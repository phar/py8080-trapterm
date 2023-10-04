import pygame
import signal
import cpu
import pickle
import time
import video
import io8080
import interface
import keybd

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


#		self._cpu.load_rom(0x0000,"roms/06204.035.bin")
#		self._cpu.load_rom(0x0400,"roms/06204.036.bin")

		self._cpu.load_rom(0x0000,"roms/debug.bin")

	def dummytimer(self,emu):
		print("beep")

	def _handle(self, event):
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c and pygame.key.get_mods() & KMOD_CTRL:
				self._keybd.set_moifier(True)
			else:
				self._keybd.key_down_ascii(event.key)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_c and pygame.key.get_mods() & KMOD_CTRL:
				self._keybd.set_moifier(False)
			else:
				self._keybd.key_up_ascii(event.key )

		
	def step(self, steps=1):
		for i in range(steps):
			isbp = self._cpu.step()
			pygame.display.update()
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
		fps_clock = pygame.time.Clock()
#		while True:
#			surface.fill(self.BLACK)
		signal.signal(signal.SIGINT, handle_interrupt)
		global break_interrupt
		break_interrupt = False
		while break_interrupt == False:
			for event in pygame.event.get():
				self._handle(event)

			for i in range(32):
				isbp,x = self.step()
				if break_interrupt == True or isbp:
					print ("breakpoint reached")
					return True

			fps_clock.tick(self._video._fps)
			pygame.display.update()
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		return -1
