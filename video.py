import pygame
import cpu
import struct
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#ASPECT_RATIO = MIN_WIDTH / MIN_HEIGHT

FONT_RESOLUTION = (8,12 )
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
		return self._cpu._memory.memory[address]

	def _refresh(self):
		"""
		Update the pixel array

		:return:
		"""
		px_array = pygame.PixelArray(self.surface)

		for j in range(0, CHAR_RESOLUTION[1]):
			for i in range(0, CHAR_RESOLUTION[0]):
				memaddr = 0xc000 + (j * CHAR_RESOLUTION[0]) + i
				
				for e in range(FONT_RESOLUTION[0]):
					for o in range(8):
						if self._char_rom[0][(self._cpu._memory.memory[memaddr] * 8)+o] & 0x01 << e:
							px_array[(i * FONT_RESOLUTION[0])+e][(j * FONT_RESOLUTION[1])+o] = WHITE
						else:
							px_array[(i * FONT_RESOLUTION[0])+e][(j * FONT_RESOLUTION[1])+o] = BLACK

						if o < 3:
							if self._char_rom[1][(self._cpu._memory.memory[memaddr] * 8)+o] & 0x01 << e:
								px_array[(i * FONT_RESOLUTION[0])+e][(j * FONT_RESOLUTION[1])+o+8] = WHITE
							else:
								px_array[(i * FONT_RESOLUTION[0])+e][(j * FONT_RESOLUTION[1])+o+8] = BLACK

		del(px_array)
		pygame.display.flip()
