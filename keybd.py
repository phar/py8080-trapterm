import random

class Keyboard:
	def __init__(self, cpu):
		self.kybd_latched = False;
		self.kybd_latched_key = 0;

		self.modifier_state = 0;
		self.key_matrix_state = 0;

		self.kybd_latch_value = 0;
		self._cpu = cpu
		
		self._cpu._io.register_ioport(0x48,"r",self.read_modifiers)
		self._cpu._io.register_ioport(0x50,"r",self.read_keyboard)


	def read_modifiers(self,port,mode,data):
		return self.modifier_state

	def read_keyboard(self,port,mode,data):
		self.kybd_latched = False
		return self.key_matrix_state
			

		
	def set_scan_code_from_ascii(self, ascii):
		return random.randint(0,255) #fixme
		
		
	def key_down_ascii(self,ascii):
		print("keydown")
		self.kybd_latched = True
		self.kybd_latched_key |= self.set_scan_code_from_ascii(ascii)
		
	def key_up_ascii(self,ascii):
		print("keyup")
		self.kybd_latched_key ^= self.set_scan_code_from_ascii(ascii)
