import cmd
import hexdump
import cpu
import opcodes

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
		"C":opcodes.FLAGS_CARRY_FLAG}


	def __init__(self,emu):
		super().__init__()
		self.emu=emu
		# Set up the signal handler for Ctrl+C

	def do_run(self,arg):
#		signal.signal(signal.SIGINT, handle_interrupt)
#		global break_interrupt
#		break_interrupt = False
#		while break_interrupt == False:
		self.emu.run()
		print("--------------------------------------\nbreak @0x%04x" % self.emu._cpu.get_regs()["pc"].value)
#		signal.signal(signal.SIGINT, signal.SIG_DFL)
		
		
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

	def do_step(self, arg):
		if arg:
			step = parse_inputint(arg)
		else:
			step = 1
		
		i,s = self.emu.step(step)
		self.do_registers(arg)
		print(s[2])
		
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
#			print(type(r[n]))
			
			if isinstance(r[n], cpu.FLAGS_REGISTER):
				print("\nFlags: 0x%02x" % v.value )
				for nn,vv in self._flagsinfo.items():
					print("  %s: 0x%x" % (nn, (v.value & vv) > 0)  )
				
			elif isinstance(r[n], cpu.REGISTER_CELL):
				print(n,"\t0x%x" % v.value, end="\t")

			if (i % 4) == 0:
				print("")
			i+=1
		print("\n")
		
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


