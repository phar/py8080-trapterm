import pygame
import cpu
import struct

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#ASPECT_RATIO = MIN_WIDTH / MIN_HEIGHT

FONT_RESOLUTION = (5,7)
CHAR_RESOLUTION = (40,16)
SCALE_FACTOR = 4

class Printer:
	def __init__(self,emucpu):
		self._cpu = emucpu

