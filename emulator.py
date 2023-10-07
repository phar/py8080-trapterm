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


def handle_interrupt(signal, frame):
	print("\nKeyboard interrupt received.")
	global break_interrupt
	break_interrupt = True
    
    

class Emulator:
	def __init__(self):
		self._cpu = cpu.CPU(self, freq=CLOCK_FREQ)
		self._video = video.TextVideoDisplay(self._cpu);
		self._interface = interface.Interface(self._cpu)
		self._keybd = keybd.Keyboard(self._cpu,interrupt=0x04)
#			self._cpu.load_rom(0x0000,path)

		self.running = False
		self._cpu.load_rom(0x0000,"roms/06204.035.bin")
		self._cpu.load_rom(0x0400,"roms/06204.036.bin")
		self._cpu._memory.set_access_callback(0,4, self.read_only_memory) #0x0000


#		self._cpu.load_rom(0x0000,"roms/debug.bin")

	def read_only_memory(self, address, value, action):
#		if action == "w":
		return self._cpu._memory.memory[address]

	def dummytimer(self,emu):
		print("beep")

	def _handle(self, event):
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
				self._keybd.set_moifier(True)
			else:
				self._keybd.key_down_ascii(event.key)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_c and pygame.key.get_mods() &  pygame.KMOD_CTRL:
				self._keybd.set_moifier(False)
			else:
				self._keybd.key_up_ascii(event.key )

		
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
			self._video.fps_clock.tick(self._video._fps)
			pygame.display.update()
			pygame.display.flip()
#			clock.tick(60)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		self.running = False
		return -1
