import struct
import io8080
from opcodes import *

class InvalidInstruction(Exception):
    pass


class StackException(Exception):
    pass


MAX_CYCLES = 0x411B

#logger = logging.getLogger('cpu')

class RAM(list):
	def __init__(self, size,pagesize=512):
	  self.size = size + 1
	  self.memory = [0] * (self.size)
	  self.pagesize = pagesize
	  self.access_callbacks = [None] * int((self.size/self.pagesize))

	def set_access_callback(self, pageno, pagecount, callback):
		for p in range(pagecount):
			self.access_callbacks[pageno + p] = callback

	def __getitem__(self, address):
		if isinstance(address, int):
			address &= 0xffff
			page = int(address / self.pagesize)
			if self.access_callbacks[page] is not None:
				return self.access_callbacks[page](address, self.memory[address], "r")
			return  self.memory[address]
		else:
			raise TypeError("Address must be an integer")

	def __setitem__(self, address, value):
		address &= 0xffff
		if isinstance(address, int) and isinstance(value, int):
			page = int(address / self.pagesize)
			if self.access_callbacks[page] is not None:
				self.memory[address] = self.access_callbacks[page](address, value, "w")
			self.memory[address] = value & 0xff
		else:
			raise TypeError("Address and data must be integers")
	  


class REGISTER_CELL:
	def __init__(self,name="", width=16):
		self.name = name
		self.val = 0
		self.bitwidth = width
	
	@property
	def value(self):
		return self.val

	@value.setter
	def value(self, val):
		if isinstance(val, int):
			self.val = val & ((2 ** self.bitwidth) - 1)
		else:
			raise TypeError("Value must be an integer")


class ACCUMULATOR_REGISTER(REGISTER_CELL):
	def __init__(self,name="", width=16):
		self.name = name
		self.val = 0
		self.bitwidth = width
		self.carry = 0
		self.aux_carry = 0
		self.zero = 0
		self.parity = 0;
		self.sign = 0
		
	@property
	def value(self):
		return self.val

	@value.setter
	def value(self, val):
		if isinstance(val, int):
			# Calculate the carry and aux_carry flags
			carry_mask =  ((2 ** self.bitwidth) - 1) + 1
			aux_carry_mask = 1 << (self.bitwidth // 2)
			
			self.carry = (val & carry_mask) > 0
			self.aux_carry = (val & aux_carry_mask) > 0
			self.parity = bin(val).count('1') % 2
			self.sign = (val & 0x80) > 0
			# Mask the value to fit within the specified bit width
			self.val = val & ((2 ** self.bitwidth) - 1)
			if self.val == 0:
				self.zero = 1
			else:
				self.zero = 0
		else:
			raise TypeError("Value must be an integer")
			

class FLAGS_REGISTER(REGISTER_CELL):
	def __init__(self,name="F",width=16):
		self.name = name
		self.val = 0
		self.bitwidth = width
		self.val &= 0b11010111   #always zero bits
		self.val |= 0b00000010	#always one bits
	

	@property
	def value(self):
		return self.val

	@value.setter
	def value(self, val):
		if  isinstance(val, int):
			self.val = val & ((2**self.bitwidth) - 1)
			self.val &= 0b11010111   #always zero bits
			self.val |= 0b00000010	#always one bits
		else:
			raise TypeError("Address and data must be integers")

class CPU:
#	VRAM_ADDRESS = 0x2400
	
	def __init__(self, parent, freq):
		self.parent = parent
		self.freq = freq
		self.registers = {
			"pc":REGISTER_CELL("pc",width=16),
			"sp":REGISTER_CELL("sp",width=16),
			"a":ACCUMULATOR_REGISTER("a",width=8),
			"f":FLAGS_REGISTER(width=8),
			"bc":REGISTER_CELL("bc",width=16),
			"de":REGISTER_CELL("de",width=16),
			"hl":REGISTER_CELL("hl",width=16),
			"cycles":REGISTER_CELL("cycles",width=64),
			"int":REGISTER_CELL("int",width=1),
			"ie":REGISTER_CELL("ie",width=1),
		}
		self.breakpoints = []
		self.timers = []
		
		self._io = io8080.IO()
		self._memory = RAM(0xffff)

	def add_timer(self, clock_ticks, callback):
		self.timers.append((clock_ticks, callback))

	@property
	def memory(self):
		return self._memory


	def load_rom(self,baseaddress,path):
		idx = baseaddress
		with open(path, 'rb') as f:
			while True:
				byte = f.read(1)
				if not byte:
					break
				a, = struct.unpack('c', byte)
				self._memory[idx] = ord(a)
				idx+=1

	def reset(self):
		"""
		Resets registers and flags
		:return:
		"""
		for n,v in self.registers.items():
			v.value =0
			
	def get_regs(self):
		"""
			return registers
		"""
		return self.registers


	def run(self):
		"""
		Starts CPU and runs a given number of cycles per frame in UI

		:return:
		"""

		for i in range(MAX_CYCLES):
			isbp = self.step()
			if self.registers["pc"].value in self.breakpoints:
				return True
		return False


#	def run_cycles(self, cycles):
#		"""
#		Used for debugging
#
#		:param cycles: int
#		:return: program counter
#		"""
##		global break_interrupt
##		for i in range(cycles):
##			isbp = self.step()
##			if break_interrupt == True or self.registers["pc"].value in self.breakpoints:
##				return True
#		return False

	def disassemble_current_instruction(self,offset):

		instruction,args = self.decompose(offset)

		c = ''
		c += "0x%04x\t" % offset
		c += instruction["opstr"]
		c += "\t"
		if len(instruction["arg"]) >0:
			if instruction["arg"][0] == "a16":
				c += "0x%04x" % args[0]
			elif instruction["arg"][0] == "d8":
				c += "0x%02x" % args[0]
			else:
				c += instruction["arg"][0]

		if len(instruction["arg"]) > 1:
			if instruction["arg"][1] == "d8":
				c += ",0x%02x" % args[1]
			elif instruction["arg"][1] == "d16":
				c += ",0x%04x" % args[1]
			else:
				c += ",%s" % instruction["arg"][1]
		return instruction,args,c
		

	
	def decompose(self, address):
		instruction = Opcodes8080[self.fetch_rom_byte(address)]
		args = []
		ret = None
		for a in instruction["arg"]:
			if len(instruction["arg"]) and instruction["type"] not in [TYPE_LOGIC_16,TYPE_MOVE_16]:
				if a == "d8":
					ret = self.fetch_rom_byte(address + 1)
				elif a == "d16":
					ret = self.fetch_rom_short(address + 1)
				elif a == "a16":
					ret = self.fetch_rom_short(address + 1)
				elif a == "A":
					ret = self.registers["a"].value
				elif a == "B":
					ret = (self.registers["bc"].value  & 0xff00) >> 8
				elif a == "C":
					ret = self.registers["bc"].value & 0x00ff
				elif a == "H":
					ret = (self.registers["hl"].value & 0xff00) >> 8
				elif a == "L":
					ret = self.registers["hl"].value  & 0x00ff
				elif a == "D":
					ret = (self.registers["de"].value  & 0xff00) >> 8
				elif a == "E":
					ret = self.registers["de"].value & 0x00ff
				elif a == "SP":
					ret = self.registers["sp"].value
				elif a == "M":
					ret = self.fetch_rom_short(self.registers["hl"].value)
				elif a == "0":
					ret = 0
				elif a == "1":
					ret = 1
				elif a == "2":
					ret = 2
				elif a == "3":
					ret = 3
				elif a == "4":
					ret = 4
				elif a == "5":
					ret = 5
				elif a == "6":
					ret = 6
				elif a == "7":
					ret = 7
			elif len(instruction["arg"]) and instruction["type"] in [TYPE_LOGIC_16,TYPE_MOVE_16]:
				if a == "d8":
					ret = self.fetch_rom_byte(address + 1)
				elif a == "d16":
					ret = self.fetch_rom_short(address + 1)
				elif a == "a16":
					ret = self.fetch_rom_short(address + 1)
				elif a == "A":
					ret = self.registers["a"].value
				elif a == "B":
					ret = self.registers["bc"].value
				elif a == "H":
					ret = self.registers["hl"].value
				elif a == "D":
					ret = self.registers["de"].value
				elif a == "SP":
					ret = self.registers["sp"].value
				elif a == "PSW":
					ret = self.registers["f"].value
				

			if ret is not None:
				args.append(ret)

		if len(args) < 2:
			args.append(None)
		if len(args) < 2:
			args.append(None)
			
		return (instruction, args)
		
	def step(self):
		"""
		Executes an instruction and updates processor state

		:return:
		"""

		try:

			instruction,args = self.decompose(self.registers["pc"].value)
		
		
		except Exception as e:
			print("An error occurred while executing opcode %s at 0x%04x" % (instruction["opstr"], self.registers["pc"].value),args)
			print(f"An error occurred: {e}")

		if instruction is not None:
			self.registers["pc"].value += instruction["l"]
			cycles = 0

			if hasattr(self, "_" + instruction["opstr"].lower()) and callable(getattr(self, "_" + instruction["opstr"].lower())):
				method = getattr(self, "_" + instruction["opstr"].lower())
				try:
					(cycles, result) = method(instruction, args[0],args[1])
				except Exception as e:
					print("An error occurred while executing opcode %s at 0x%04x %s" % (instruction["opstr"], self.registers["pc"].value,args) )
					print(f"An error occurred: {e}")
					
					
				if instruction["type"]  in [TYPE_LOGIC_8]:
					self.flag_state(FLAGS_CARRY_FLAG, self.registers["a"].carry)
					self.flag_state(FLAGS_ZERO_FLAG, self.registers["a"].zero)
					self.flag_state(FLAGS_AUXCARRY_FLAG, self.registers["a"].aux_carry)
					self.flag_state(FLAGS_PARITY_FLAG, self.registers["a"].parity)
					self.flag_state(FLAGS_SIGN_FLAG, self.registers["a"].sign)

				
				if len(instruction["arg"]) and instruction["type"] not in [TYPE_LOGIC_16,TYPE_MOVE_16]:
#				try:
						if instruction["arg"][0] == "A":
							self.registers["a"].value = result
						elif instruction["arg"][0] == "SP":
							self.registers["sp"].value  = result
						elif instruction["arg"][0] == "B":
							self.registers["bc"].value  &= 0x00ff
							self.registers["bc"].value  |= result << 8
						elif instruction["arg"][0] == "C":
							self.registers["bc"].value  &= 0xff00
							self.registers["bc"].value  |= result
						elif instruction["arg"][0] == "H":
							self.registers["hl"].value  &= 0x00ff
							self.registers["hl"].value  |= result << 8
						elif instruction["arg"][0] == "L":
							self.registers["hl"].value  &= 0xff00
							self.registers["hl"].value  |= result
						elif instruction["arg"][0] == "D":
							self.registers["de"].value  &= 0x00ff
							self.registers["de"].value  |= result << 8
						elif instruction["arg"][0] == "E":
							self.registers["de"].value  &= 0xff00
							self.registers["de"].value  |= result
						elif instruction["arg"][0] == "M":
							self._memory[self.registers["hl"].value] = result & 0xff
	#				except:
	#					print("ERROR!",instruction)
				elif len(instruction["arg"]) and instruction["type"] in [TYPE_LOGIC_16,TYPE_MOVE_16]:
					if instruction["arg"][0] == "SP":
						self.registers["sp"].value  = result
					elif instruction["arg"][0] == "B":
						self.registers["bc"].value  = result
					elif instruction["arg"][0] == "H":
						self.registers["hl"].value = result
					elif instruction["arg"][0] == "D":
						self.registers["de"].value = result
					elif instruction["arg"][0] == "PSW":
						self.registers["f"].value = result

				
				for (clocks,cb) in self.timers:
					if ((self.registers["cycles"].value + cycles) % clocks) < cycles:
						cb(self.parent)

				self.registers["cycles"].value += cycles

			else:
				print("UNHANDLED2!", instruction["opstr"])

		if self.registers["pc"].value in self.breakpoints:
			return True
		else:
			return False


	def call_interrupt(self, number):
		print("Interrupt %d" % number)
		self._push( None, self.registers["pc"].value)
		self._rst(None,number,None)

	def _nop(self, op,  a0=None, a1=None):
		return (op["c"][0], None)
		

	def _lxi(self, op,  a0=None, a1=None):
		return (op["c"][0], a1)

	def _mov(self, op,  a0=None, a1=None):
		return (op["c"][0], a1)
	
	def _cpi(self, op,  a0=None, a1=None):
		self.registers["a"].value -= a0
		return (op["c"][0], self.registers["a"].value)

	def _ani(self, op,  a0=None, a1=None):
		self.registers["a"].value &= a0
		return (op["c"][0], self.registers["a"].value)

	def _ora(self, op,  a0=None, a1=None):
		self.registers["a"].value |= a0
		return (op["c"][0],self.registers["a"].value)

	def _ori(self, op,  a0=None, a1=None):
		self.registers["a"].value |= a0
		return (op["c"][0],self.registers["a"].value)
		
	def _ana(self, op,  a0=None, a1=None):
		self.registers["a"].value &= a0
		return (op["c"][0], self.registers["a"].value)

	def _sub(self, op,  a0=None, a1=None):
		self.registers["a"].value -= a0
		return (op["c"][0], self.registers["a"].value )

	def _add(self, op,  a0=None, a1=None):
		self.registers["a"].value += a0
		return (op["c"][0], self.registers["a"].value)

	def _dad(self, op,  a0=None, a1=None):
		self.registers["hl"].value += a0
		return (op["c"][0], a0)


	def _dcr(self, op,  a0=None, a1=None):
		return (op["c"][0], a0 - 1)


	def _adc(self, op,  a0=None, a1=None):
		self.registers["a"].value += (a0 + sself.get_flag(FLAGS_CARRY_FLAG))
		return (op["c"][0], self.registers["a"].value)

	def _xri(self, op,  a0=None, a1=None):
		self.registers["a"].value ^= a0
		return (op["c"][0], self.registers["a"].value)

	def _xra(self, op,  a0=None, a1=None):
		self.registers["a"].value ^= a0
		return (op["c"][0], self.registers["a"].value)

	def _sta(self, op,  a0=None, a1=None):
		self._memory[a0] = self.registers["a"].value
		return (op["c"][0], None)
		
	def _ral(self, op,  a0=None, a1=None):
		if self.registers["a"].value & 0x80:
			c = 1
		else:
			c = 0
		self.registers["a"].value = (self.registers["a"].value << 1) | self.get_flag(FLAGS_CARRY_FLAG)
		self.flag_state(FLAGS_CARRY_FLAG,c)
		return (op["c"][0], None)

	def _rar(self, op,  a0=None, a1=None):
		if self.registers["a"].value & 0x01:
			c = 1
		else:
			c = 0
		self.registers["a"].value = (self.registers["a"].value >> 1) | (self.get_flag(FLAGS_CARRY_FLAG) << 7)
		self.flag_state(FLAGS_CARRY_FLAG,c)
		return (op["c"][0], None)
		

	def _rrc(self, op,  a0=None, a1=None):
		if self.registers["a"].value & 0x01:
			c = 1
		else:
			c = 0
		self.registers["a"].value = (self.registers["a"].value >> 1) | (c << 7)
		self.flag_state(FLAGS_CARRY_FLAG,c)
		return (op["c"][0], None)

	def _rlc(self, op,  a0=None, a1=None):
		if self.registers["a"].value & 0x80:
			c = 1
		else:
			c = 0
		self.registers["a"].value = (self.registers["a"].value << 1) | c
		self.flag_state(FLAGS_CARRY_FLAG,c)
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], None)

	def _jc(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_CARRY_FLAG):
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], a1)

	def _jmp(self, op,  a0=None, a1=None):
		self.registers["pc"].value = a0
		return (op["c"][0], a1)

	def _jz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG):
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], a1)

	def _jnz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG) == 0:
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], a1)
		
	def _jnc(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_CARRY_FLAG) == 0:
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], a1)
		
	def _jc(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_CARRY_FLAG):
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], a1)

	def _rst(self, op,  a0=None, a1=None):
		self.registers["pc"].value = a0 * 8
		if op == None:
			return None
		return (op["c"][0], None)

	def _cmp(self, op,  a0=None, a1=None):
		return (op["c"][0], (self.registers["a"].value - a0))

	def _lda(self, op,  a0=None, a1=None):
		self.registers["a"].value = a0
		return (op["c"][0], a1)

	def _ldax(self, op,  a0=None, a1=None):
		if op["arg"][0] == "B":
			self.registers["a"].value = self.fetch_rom_short(self.registers["bc"].value)
		elif op["arg"][0] == "D":
			self.registers["a"].value = self.fetch_rom_short(self.registers["de"].value)
		return (op["c"][0], a0)

	def _mvi(self, op,  a0=None, a1=None):
		return (op["c"][0], a1)

	def _inx(self, op,  a0=None, a1=None):
		return (op["c"][0], a0+1)

	def _dcx(self, op,  a0=None, a1=None):
		return (op["c"][0], a0+1)

	def _ei(self, op,  a0=None, a1=None):
		self.registers["ie"].value = 1
		return (op["c"][0], None)

	def _di(self, op,  a0=None, a1=None):
		self.registers["ie"].value = 0
		return (op["c"][0], None)

	def _inr(self, op,  a0=None, a1=None):
		return (op["c"][0], a0 + 1)

	def _adi(self, op,  a0=None, a1=None):
		self.registers["a"].value += a0
		return (op["c"][0], self.registers["a"].value)

	def _sui(self, op,  a0=None, a1=None):
		self.registers["a"].value -= a0
		return (op["c"][0], self.registers["a"].value)

	def _shld(self, op,  a0=None, a1=None): #fixme
		self._memory[a0] = self.registers["hl"].value
		return (op["c"][0], None)

	def _cma(self, op,  a0=None, a1=None): #fixme
		self.registers["a"].value -= ~self.registers["a"].value
		return (op["c"][0], self.registers["a"].value)
		
	def _lhld(self, op,  a0=None, a1=None): #fixme
		self.registers["hl"].value = self._memory[a0]
		return (op["c"][0], None)

	def _xchg(self, op,  a0=None, a1=None):
		t = self.registers["hl"].value
		self.registers["hl"].value = self.registers["de"].value
		self.registers["de"].value = t
		return (op["c"][0], None)
		
	def _push(self, op,  a0=None, a1=None):
		self._memory[self.registers["sp"].value - 1] = (a0 & 0xff00) >> 8
		self._memory[self.registers["sp"].value - 2] = (a0 & 0x00ff)
		self.registers["sp"].value -= 2
		if op == None:
			return
		return (op["c"][0], a0)

	def _call(self, op,  a0=None, a1=None):
		self._push(None, self.registers["pc"].value)
		self.registers["pc"].value = a0
		return (op["c"][0], None)
		
	def _cnz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG) == 0:
			self._push(None, self.registers["pc"].value,None)
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)

	def _cz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG) == 1:
			self._push(None, self.registers["pc"].value)
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)


	def _cpe(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_PARITY_FLAG) == 1:
			self._push(None, self.registers["pc"].value,None)
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)


	def _cm(self, op,  a0=None, a1=None): #fixme
		if self.get_flag(FLAGS_SIGN_FLAG) == 1:
			self._push(None, self.registers["pc"].value,None)
			self.registers["pc"].value = a0
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)

	def _ret(self, op,  a0=None, a1=None):
		self.registers["pc"].value = self._pop(None,None,None)
		return (op["c"][0], None)

	def _rz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG) == 1:
			self.registers["pc"].value = self._pop(None,None,None)
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)

	def _rnz(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_ZERO_FLAG) == 0:
			self.registers["pc"].value = self._pop(None,None,None)
		return (op["c"][self.get_flag(FLAGS_ZERO_FLAG)], None)

	def _rc(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_CARRY_FLAG) == 1:
			self.registers["pc"].value = self._pop(None,None,None)
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], None)

	def _rnc(self, op,  a0=None, a1=None):
		if self.get_flag(FLAGS_CARRY_FLAG) == 0:
			self.registers["pc"].value = self._pop(None,None,None)
		return (op["c"][self.get_flag(FLAGS_CARRY_FLAG)], None)

	def _pop(self, op,  a0=None, a1=None):
		r = self.fetch_rom_short(self.registers["sp"].value)
		self.registers["sp"].value += 2
		if op == None:
			return r
		return (op["c"][0], r)

	def _out(self, op,  a0=None, a1=None):  #fixme
		self._io.output(a0, self.registers["a"].value)
		return (op["c"][0],  self.registers["a"].value)
		
	def _in(self, op,  a0=None, a1=None):  #fixme
		self.registers["a"].value = self._io.input(a0)
		return (op["c"][0], None)

########################################################

	def set_flag(self, flag):
		self.registers["f"].value |= flag

	def get_flag(self, flag):
		if self.registers["f"].value & flag > 0:
			return 1
		else:
			return 0
		
	def clear_flag(self, flag):
		self.registers["f"].value &= ~flag

	def flag_state(self, flag, state):
		if state > 0:
			self.registers["f"].value |= flag
		else:
			self.registers["f"].value &= ~flag

	def read_byte(self, address):
		byte_ = self._memory[address]
		if byte_ > 0xFF:
			raise ValueError(
				'{} is not a valid byte at {}'.format(byte_, address))

		return byte_

	def read_2bytes(self, address):
		return (self._memory[address + 1] << 8) + self._memory[address]

	def write_byte(self, address, data):
		self._memory[address] = data & 0xFF

	def write_2bytes(self, address, data):
		self._memory[address + 1] = data >> 8
		self._memory[address] = data & 0xFF


	def fetch_rom_byte(self,address):
		# Read next 8 bits
		data = self._memory[address]
		return data

	def fetch_rom_short(self,address):
		# Read next 16 bits (notice endian)
		data = (self._memory[address + 1] << 8) + self._memory[address]
		return data



	def fetch_rom_next_byte(self,address=None):
		# Read next 8 bits
		data = self.fetch_rom_byte(self.registers["pc"].value)
		return data

	def fetch_rom_next_2bytes(self):
		# Read next 16 bits (notice endian)
#		data = (self._memory[self.registers["pc"].value + 1] << 8) + self._memory[self.registers["pc"].value]
		data = self.fetch_rom_short(self.registers["pc"].value)
		return data

