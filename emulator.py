import pygame
import signal
import cpu
import pickle
import time
import video
import io8080
import interface
import keybd
import json
#MIN_WIDTH = 256
#MIN_HEIGHT = 224
CLOCK_FREQ = 4000000

import pygame
def handle_interrupt(signal, frame):
	print("\nKeyboard interrupt received.")
	global break_interrupt
	break_interrupt = True
    
    

class Emulator:
	def __init__(self,profile="entrex.def"):
		pygame.init()
		pygame.mixer.init()

		self.fps_clock = pygame.time.Clock()

		self._cpu = cpu.CPU(self, freq=CLOCK_FREQ)
		self._video = video.TextVideoDisplay(self._cpu);
		self._interface = interface.Interface(self._cpu)
		self._keybd = keybd.Keyboard(self._cpu,interrupt=0x04)
		self.running = False
		
		try:
			f = open(profile,"r")
			self.profile = json.load(f)
			f.close()
		except:
				self.profile = {}

		#onboard rom sockets
		if "BOOT_ROM_LOW" in  self.profile and self.profile["BOOT_ROM_LOW"] != "":
			self._cpu.load_rom(0x0000, self.profile["BOOT_ROM_LOW"])
		if "BOOT_ROM_HIGH" in  self.profile and self.profile["BOOT_ROM_HIGH"] != "":
			self._cpu.load_rom(0x0400,self.profile["BOOT_ROM_HIGH"])
		self._cpu._memory.set_access_callback(0,4, self.read_only_memory) #0x0000

		#ram/rom card sockets
		if "AUX_ROM_SLOT_0" in  self.profile and self.profile["AUX_ROM_SLOT_0"] != "":
			self._cpu.load_rom(0x0800,self.profile["AUX_ROM_SLOT_0"])
		if "AUX_ROM_SLOT_1" in  self.profile and self.profile["AUX_ROM_SLOT_1"] != "":
			self._cpu.load_rom(0x0900,self.profile["AUX_ROM_SLOT_1"])
		if"AUX_ROM_SLOT_2" in  self.profile and  self.profile["AUX_ROM_SLOT_2"] != "":
			self._cpu.load_rom(0x9a00,self.profile["AUX_ROM_SLOT_2"])
		if "AUX_ROM_SLOT_3" in  self.profile and self.profile["AUX_ROM_SLOT_3"] != "":
			self._cpu.load_rom(0x0b00,self.profile["AUX_ROM_SLOT_3"])
		if "AUX_ROM_SLOT_4" in  self.profile and self.profile["AUX_ROM_SLOT_4"] != "":
			self._cpu.load_rom(0x0c00,self.profile["AUX_ROM_SLOT_4"])
		if "AUX_ROM_SLOT_5" in  self.profile and  self.profile["AUX_ROM_SLOT_5"] != "":
			self._cpu.load_rom(0x0d00,self.profile["AUX_ROM_SLOT_5"])
		self._cpu._memory.set_access_callback(4,10, self.read_only_memory) #0x0000


	def read_only_memory(self, address, value, action):
		return self._cpu._memory.memory[address]

	def _handle(self, event):
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
#			if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
#				self._keybd.set_moifier(True)
#			else:
				self._keybd.key_down_event(event)

		if event.type == pygame.KEYUP:
#			if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
#				self._keybd.set_moifier(False)
#			else:
				self._keybd.key_up_event(event)

		
	def step(self, steps=1):
		for i in range(steps):
			isbp = self._cpu.step()
			if isbp and i < steps:
					print ("breakpoint reached")
					break

		return isbp, self._cpu.disassemble_current_instruction(self._cpu.registers["pc"].value) 

	
	def run(self, debug=False):
		"""
		Sets up display and starts game loop

		:return:
		"""

#		pygame.init()
#		surface = pygame.display.set_mode(self._display_size)
#		caption = self.CAPTION_FORMAT.format('')
#		pygame.display.set_caption(caption)
#
#		surface.fill(self.BLACK)
#		self._px_array = pygame.PixelArray(surface)
#
#		pygame.display.update()
		self.running = True
#		fps_clock = pygame.time.Clock()
#		while True:
#			surface.fill(self.BLACK)
		signal.signal(signal.SIGINT, handle_interrupt)
		global break_interrupt
		break_interrupt = False
		while break_interrupt == False:
			for event in pygame.event.get():
				self._handle(event)
#				print(event)
			for i in range(128):
				isbp,x = self.step()
				if break_interrupt == True or isbp:
					print ("breakpoint reached")
					self.running = False
					return True

			self._video._refresh()
			self.fps_clock.tick(self._video._fps)
			pygame.display.update()
			pygame.display.flip()
#			clock.tick(60)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.running = False
		return -1
