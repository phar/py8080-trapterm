import random

class Keyboard:
	def __init__(self, cpu, interrupt):
		self.kybd_latched = False
		self.kybd_latched_key = 0
		self.led_state = False
		self.modifier_state = 0
		self.key_matrix_state = 0
		self.interrupt_no = interrupt & 0x0f
		self.kybd_latch_value = 0
		self._cpu = cpu
		
		self._cpu._io.register_ioport(0x48,"r",self.read_modifiers)
		self._cpu._io.register_ioport(0x50,"r",self.read_keyboard)

	def set_moifier(self, mod):
		self.modifier_state = mod

	def set_LED(self, led):
		self.led_state = led


	def read_modifiers(self,port,mode,data):
		return self.modifier_state

	def read_keyboard(self,port,mode,data):
		self.kybd_latched = False
		ascii = self.kybd_latched_key
		self.kybd_latched_key = 0
		
		return ascii

	def key_down_ascii(self,ascii):
		self.kybd_latched = True
		self.kybd_latched_key = ascii
		self._cpu.call_interrupt(self.interrupt_no)
		
	def key_up_ascii(self,ascii):
		pass
