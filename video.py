import pygame
import cpu
import struct
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#ASPECT_RATIO = MIN_WIDTH / MIN_HEIGHT

FONT_RESOLUTION = (8,8 )
CHAR_RESOLUTION = (40,16)
SCALE_FACTOR = 1




class TextVideoDisplay:
	def __init__(self,emucpu, width=CHAR_RESOLUTION[0],height=CHAR_RESOLUTION[1]):
		
#		self._memory = cpu.RAM((CHAR_RESOLUTION[0] * FONT_RESOLUTION[0]) * (CHAR_RESOLUTION[1] * FONT_RESOLUTION[1])+1) #fixme
#		self._memory = [0] * ((CHAR_RESOLUTION[0] * FONT_RESOLUTION[0]) * (CHAR_RESOLUTION[1] * FONT_RESOLUTION[1])+1)
		self._char_rom = [self.open_rom("roms/90288-002.bin"),self.open_rom("roms/90288-003.bin")]
		self._display_size = ((CHAR_RESOLUTION[0] * FONT_RESOLUTION[0]) , (CHAR_RESOLUTION[1] * FONT_RESOLUTION[1]))
		pygame.init()
		
		
		self.surface = pygame.display.set_mode(self._display_size)

		self.surface.fill(BLACK)

		self.CAPTION_FORMAT = 'TrapTerm: {}'

		caption = self.CAPTION_FORMAT.format('')
		pygame.display.set_caption(caption)

		pygame.display.update()
#		fps_clock = pygame.time.Clock()

		self._width = width
		self._height = height
		self._fps = 30
		self._char_rom_sel = 0
		self._cpu = emucpu
		self._base_page = 0x60 #0xC000
#		self.base_address_end = 0x8fff
		self._page_count = 4

		self._cpu._memory.set_access_callback(self._base_page,self._page_count, self.display_access) #0xc000

	def open_rom(self,path):
		ret = []
		with open(path, 'rb') as f:
			while True:
				byte = f.read(1)
				if not byte:
					break
				a, = struct.unpack('c', byte)
				ret.append(ord(a))
		return ret

	def open_display(self):
		pass

	def display_access(self, address, value, action):
		if action == "w":
			self._refresh()
		print("access display %04x" % address)
		return self._cpu._memory.memory[address]

	def _refresh(self):
		"""
		Update the pixel array

		:return:
		"""
		px_array = pygame.PixelArray(self.surface)

		for i in range(0,self._display_size[0], FONT_RESOLUTION[0]):
			for j in range(0,self._display_size[1] ,FONT_RESOLUTION[1]):
				memaddr = 0xc000 + int( ((i / FONT_RESOLUTION[0]) *CHAR_RESOLUTION[0]) + (j / FONT_RESOLUTION[1]) )
#				memaddr = int(0xc050)
				for e in range(FONT_RESOLUTION[0]):
					for o in range(FONT_RESOLUTION[1]):
#						self._cpu._memory.memory[memaddr] = ord("H")
						if self._char_rom[0][(self._cpu._memory.memory[memaddr] * FONT_RESOLUTION[0])+e] & 0x01 << o:
							px_array[i+o][j+e] = WHITE
						else:
							px_array[i+o][j+e] = BLACK

		del(px_array)

    # Update the display
		pygame.display.flip()
#```