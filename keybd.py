import random
import numpy as np

import pygame

class Keyboard:
	def __init__(self, cpu, interrupt):
		self.joystick_state = 0x00

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
		self.set_keyboard_led(False)

		self._cpu._io.register_ioport(0x01,"r",self.read_joystick)


	def set_keyboard_led(self,state):
		if state:
			self.CAPTION_FORMAT = '🔴 TrapTerm: {}'
			caption = self.CAPTION_FORMAT.format('')
			self.ledstate = True

		else:
			self.CAPTION_FORMAT = 'TrapTerm: {}'
			caption = self.CAPTION_FORMAT.format('')
			self.ledstate = False

		pygame.display.set_caption(caption)
		pygame.display.update()
		

	def set_moifier(self, mod):
		self.modifier_state = mod

	def set_LED(self, led):
		self.led_state = led


	def read_modifiers(self,port,mode,data):
		return (self.kybd_latched_key << 7) | self.modifier_state

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


	def play_sine_wave(frequency=440, duration=.25, sample_rate=44100):
		t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
		sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

		sine_wave = np.int16(sine_wave * 32767)
		sine_sound = pygame.mixer.Sound(sine_wave)
		sine_sound.play()
#		pygame.time.delay(int(duration * 1000))


	def read_joystick(self,port,mode,data):
		return self.joystick_state

	def key_down_event(self,event):
		if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
			self.set_moifier(True)
		else:

			if event.key == pygame.K_c:
				joystick_state |= 0x01
			if event.key == pygame.K_1:
				joystick_state|= 0x04
			if event.key == pygame.K_SPACE:
				joystick_state |= 0x10
			if event.key == pygame.K_LEFT:
				joystick_state |= 0x20
			if event.key == pygame.K_RIGHT:
				joystick_state  |= 0x40
	
			self.key_down_ascii(event.key)
				
				
	def key_up_event(self,event):
		if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
			self.set_moifier(True)
		else:

			if event.key == pygame.K_c:
				joystick_state &= 255 - 0x01
			if event.key == pygame.K_1:
				joystick_state &= 255 - 0x04
			if event.key == pygame.K_SPACE:
				joystick_state &= 255 - 0x10
			if event.key == pygame.K_LEFT:
				joystick_state  &= 255 - 0x20
			if event.key == pygame.K_RIGHT:
				joystick_state &= 255 - 0x40
				
			self.key_up_ascii(event.key)
			
