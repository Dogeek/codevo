import pygame
from pygame.locals import *
import math

from . import *
#from .functions import *
#from .constants import *

class UiEntity(pygame.sprite.Sprite):
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self, uiEntityGroup)
		self.heart_sprites = []
		heart_spritesheet = pygame.image.load(PATH+"sprites/ui/hearts.png").convert()
		self.magic_bar_sprite = pygame.image.load(PATH+"sprites/ui/magicbar.png").convert()
		self.magic_bar_sprite.set_colorkey((0, 255, 0))
		self.magic_sprite = pygame.image.load(PATH+"sprites/ui/magic.png").convert()
		self.magic_sprite.set_colorkey((255, 0, 255))
		for i in range(4):
			X = i*32
			surf = pygame.Surface((32, 32))
			surf.blit(heart_spritesheet, (0,0), (X, 0, 32, 32))
			#surf.set_colorkey((255, 0, 255))
			self.heart_sprites.append(surf)
		self.hearts = player.health/4
		self.player_magic = player.magic
		self.update()
		
	def update(self):
		self.surface = pygame.Surface((max(int(math.ceil(self.hearts))*32, 104), 58))
		self.surface.fill((255, 0, 255))
		hearts_full = int(math.floor(self.hearts))
		leftover = self.hearts - hearts_full
		for i in range(hearts_full):
			self.surface.blit(self.heart_sprites[0], (i*32, 0))
		if leftover == 0.25:
			self.surface.blit(self.heart_sprites[3], (leftover*32, 0))
		elif leftover == 0.5:
			self.surface.blit(self.heart_sprites[2], (leftover*32, 0))
		elif leftover == 0.75:
			self.surface.blit(self.heart_sprites[1], (leftover*32, 0))
		for i in range(self.player_magic):
			self.surface.blit(self.magic_sprite, (i+2, 22))
		self.surface.blit(self.magic_bar_sprite, (0, 22))
		self.surface.set_colorkey((255, 0, 255))
