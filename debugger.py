import cmd
import hexdump
import cpu
import opcodes
import time
import threading
import pygame
break_interrupt = False
		

class Debugger(cmd.Cmd):
	intro = 'Type help or ? to list commands.\n'
	prompt = '(debug) '
	file = None
	_flagsinfo = {
		"S":opcodes.FLAGS_SIGN_FLAG,
		"Z":opcodes.FLAGS_ZERO_FLAG,
		"AC":opcodes.FLAGS_AUXCARRY_FLAG,
		"P":opcodes.FLAGS_PARITY_FLAG,
		"CY":opcodes.FLAGS_CARRY_FLAG}


	def handle_inputs_while_debuggins(self):
		if self.emu.running == False:
			for event in pygame.event.get():
				pygame.event.get()
			self.emu._video.fps_clock.tick(self.emu._video._fps)
			pygame.display.update()
			pygame.display.flip()
			
	def __init__(self,emu):
		super().__init__()
		self.emu=emu
		timer = threading.Timer(.2, self.handle_inputs_while_debuggins)
		timer.start()		# Set up the signal handler for Ctrl+C

	def do_hexload(self,arg):
		try:
			t = arg.split(" ")
			offset = parse_inputint(t[0])
			bytes = bytearray.fromhex(" ".join(t[1:]).replace(" ", ""))
			for l in range(len(bytes)):
				self.emu._cpu.memory.memory[offset+l] = bytes[l]
		except ValueError:
			print("bad input")
			return False


	def do_run(self,arg):
#		signal.signal(signal.SIGINT, handle_interrupt)
#		global break_interrupt
#		break_interrupt = False
#		while break_interrupt == False:
		self.emu.run()
		self.do_registers(arg)
		
		ins,a,s = self.emu._cpu.disassemble_current_instruction(self.emu._cpu.registers["pc"].value)
		print(s)
		
	def do_disassemble(self,args):
		try:
			(offset,length) = args.split(" ")
			offset = parse_inputint(offset)
			length = parse_inputint(length)
		except ValueError:
			print("not enough arguments provided")
			return False
		
		o = offset
		for i in range(length):
			ins,a,s = self.emu._cpu.disassemble_current_instruction(o)
			print(s)
			o += ins["l"]


	def do_savestate(self,args):
		self.emu._cpu.save_state(args)


	def do_loadstate(self,args):
		self.emu._cpu.load_state(args)


	def do_int(self, arg):
		try:
			if arg:
				step = parse_inputint(arg)
			else:
				return
				
			self.emu._cpu.call_interrupt(step)
		except:
			print("failed")
			
	def do_step(self, arg):
		if arg:
			step = parse_inputint(arg)
		else:
			step = 1
			
		t1 = time.time()
		i,s = self.emu.step(step)
		t2 = time.time() - t1
		self.do_registers(arg)
		ins,a,s = self.emu._cpu.disassemble_current_instruction(self.emu._cpu.registers["pc"].value)
		print(s," %s Seconds" % t2)
		
	def do_break(self, arg):
		if arg:
			bp = parse_inputint(arg)
			self.emu._cpu.breakpoints.append(bp)
		else:
			print("bad bp")
			
	def do_registers(self, arg):
		r = self.emu._cpu.get_regs()
		i = 0
		for n,v in r.items():
			fmt = "\t0x%0"+str(int(v.bitwidth/4))+"x"
			print(n,fmt % v.value, end="\t")
			if (i>0) and (i % 4) == 0:
				print("")
			i+=1
			
		print("\nFlags: 0x%02x" % r["f"].value )
		for nn,vv in self._flagsinfo.items():
			print("  %s: 0x%x" % (nn, (r["f"].value & vv) > 0) ,end='' )

		print("\n")
		
	def do_set(self, args):
		try:
			(valname,value) = args.split(" ")
			valueint = parse_inputint(value)

			if valname in ["a","bc","de","hl","sp","pc"]:
				self.emu._cpu.registers[valname].value = valueint & 0xffff
				
			elif valname in ["c","e",""]:
				valref = {"c":"bc","e":"de","l":"hl"}
				self.emu._cpu.registers[valname].value &= 0xff00
				self.emu._cpu.registers[valname.lower].value |= (valueint & 0xff)

			elif  valname in ["b","d","h"]:
				valref = {"b":"bc","d":"de","h":"hl"}
				self.emu._cpu.registers[valname.lower()].value &= 0x00ff
				self.emu._cpu.registers[valname.lower()].value |=  (valueint & 0xff) << 8
				
			elif valname in ["f"]:
				self.emu._cpu.registers[valname.lower()].value = (valueint & 0xff)

			elif valname in ["S","Z","AC","CY","P"]:
				if valueint == 0:
					self.emu._cpu.registers[valname.lower()].value &= ~self._flagsinfo[valname.upper()]
				else:
					self.emu._cpu.registers[valname.lower()].value |= self._flagsinfo[valname.upper()]


			elif parse_inputint(valname) > 0:
				self.emu._cpu._memory[parse_inputint(valname)] = valueint & 0xff

		except ValueError:
			print("not enough arguments provided")
			return False
	
	def do_reset(self,args):
		self.emu._cpu.reset()
		
	def do_hexdump(self,args):
		try:
			(offset,length) = args.split(" ")
			offset = parse_inputint(offset)
			length = parse_inputint(length)
		except ValueError:
			print("not enough arguments provided")
			return False

		print(offset)
		print(length)
		copyout = []
		for i in range(offset,offset+length):
			a = self.emu._cpu._memory.memory[i]
			copyout.append(a.to_bytes(1,'big'))
		print("offset:0x%04x\n---------------------------------------------------------------------------" % offset)
		hexdump.hexdump(b"".join(copyout))
		
		
	def precmd(self, line):
		line = line.lower()
		if self.file and 'playback' not in line:
			print(line, file=self.file)
		return line
		
	def close(self):
		if self.file:
			self.file.close()
			self.file = None

def parse_inputint(input_str):
    # Check if the input string starts with '0b' and contains only 0s and 1s (binary).
    if input_str.startswith('0b') and all(char in '01' for char in input_str[2:]):
        return int(input_str, 2)
    
    # Check if the input string starts with '0x' and contains valid hexadecimal characters.
    if input_str.startswith('0x') and all(char in '0123456789abcdefABCDEF' for char in input_str[2:]):
        return int(input_str, 16)
    
    # Check if the input string represents a regular integer.
    if input_str.isdigit() or (input_str[0] == '-' and input_str[1:].isdigit()):
        return int(input_str)
    
    # If none of the above conditions match, raise an exception or return a default value.
    raise ValueError("Invalid input format")


