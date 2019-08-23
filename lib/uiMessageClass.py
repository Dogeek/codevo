import pygame
from pygame.locals import *

from . import *

class UIMessage():
	def __init__(self, text):
		self.text = text.split("\n")
		self.font_size = 20
		self.render()
		pass

	def render(self):
		self.font = pygame.font.Font(None, self.font_size)
		self.height = len(self.text)*(self.font_size+2)
		self.surface = pygame.Surface((SCREEN_WIDTH, self.height))
		top = pygame.image.load('sprites/ui/messagebox_top.png').convert()
		mid = pygame.image.load('sprites/ui/messagebox_middle.png').convert()
		bot = pygame.image.load('sprites/ui/messagebox_bot.png').convert()
		part_height = 15
		self.surface.blit(top, (0,0))
		for i in range(part_height, self.height-part_height, part_height):
			self.surface.blit(mid, (0, i))
		self.surface.blit(bot, (0,self.height-part_height))
		to_blit = [self.font.render(t, False, (255,255,255)) for t in self.text]
		for i in range(len(to_blit)):
			b = to_blit[i]
			self.surface.blit(b, (20, i*(self.font_size+2)))
		return self.surface
