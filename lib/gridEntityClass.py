import pygame
from pygame.locals import *

from . import *

class GridEntity(pygame.sprite.Sprite):
	def __init__(self, info, x, y, number_on_grid):
		pygame.sprite.Sprite.__init__(self, gridEntitiesGroup)
		self.x = x
		self.y = y
		self.pos_on_grid = number_on_grid
		self.id = info["id"]
		self.width = GRIDENTITY_WIDTH
		self.height = GRIDENTITY_HEIGHT
		spritesheet = pygame.image.load(PATH+GRIDENTITIES_FOLDER+info["sprite"]).convert()
		self.can_pass = info["can_pass"]
		self.health = info["health"]
		self.current_frame = 0
		self.index = 0
		self.num_frames = info["num_frames"]
		Y = 0
		self.frames = []
		for i in range(self.num_frames):
			X = i*self.width
			surf = pygame.Surface((self.width, self.height))
			surf.blit(spritesheet, (0,0), (X, Y, self.width, self.height))
			surf.set_colorkey((255, 0, 255))
			self.frames.append(surf)
		self.image = self.frames[0]
		self.rect = self.image.get_bounding_rect()
		self.rect.x = x*32
		self.rect.y = y*32
		self.rect.w = self.width
		self.rect.h = self.height
		self.frame_time = 2
		self.animated = (self.num_frames != 1)
		self.has_been_updated = True
		self.is_transparent = info["is_transparent"]
		self.weight = info["weight"]
		if not self.can_pass:
			gridEntitiesGroupBlocking.add(self)
		if self.animated:
			gridEntitiesGroupUpdate.add(self)
		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		if self.animated:
			self.current_frame += 1
			if self.current_frame % self.frame_time == 0:
				self.index = (self.index + 1) % len(self.frames)
				self.image = self.frames[self.index]
				self.has_been_updated = True
