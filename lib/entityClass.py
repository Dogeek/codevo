import pygame
from pygame.locals import *
from pymunk.vec2d import Vec2d as Vector2

from . import *

class Entity(pygame.sprite.Sprite):
	def __init__(self, filename, tilemap, id_):
		pygame.sprite.Sprite.__init__(self, entitiesGroup)
		self.tilemap = tilemap
		self.speed = Vector2(0, 0)
		self.index = 0
		self.direction = DOWN
		self.current_frame = 0
		self.MoveSpeed = 7
		self.filename = filename if "yaml" in filename else filename+".yaml" 
		self.id = id_
		self.path = None
		self.init_from_file()
	
	def init_from_file(self):
		data = load('config/{}'.format(self.filename))
		self.name = data["name"]
		self.health = data["health"]
		self.magic = data["magic"]
		anim = load(data["animation"])
		self.width = anim["width"]
		self.height = anim["height"]
		self.frames = []
		spritesheet = pygame.image.load(PATH+anim["spritesheet"])
		for d in anim["directions"]:
			Y = self.height * d
			tmp = []
			for i in range(anim["num_frames"]):
				X = i*self.width
				surf = pygame.Surface((self.width, self.height))
				surf.blit(spritesheet, (0,0), (X, Y, self.width, self.height))
				surf.set_colorkey(tuple(anim["colorkey"]))
				tmp.append(surf)
			self.frames.append(tmp)
		self.frame_time = anim["frame_time"]
		self.image = self.frames[0][0]
		self.sprite_rect = self.frames[0][0].get_bounding_rect().move(128, 380)
		t = (self.sprite_rect.midleft[0] + 3, self.sprite_rect.midleft[1]+8)
		self.rect = pygame.Rect(t, (self.sprite_rect.w-7, int(self.sprite_rect.h/4)-1))
		self.inventory = data["inventory"]
		self.mask = pygame.mask.from_surface(self.image)
		self.position = Vector2(self.rect.center)
		self.grid_position = pos_to_grid(self.position)
		pass
	
	def update(self):
		self.position = Vector2(self.rect.center)
		self.grid_position = pos_to_grid(self.position)
		if self.speed != Vector2(0,0):
			self.current_frame += 1
			if self.current_frame % self.frame_time == 0:
				self.index = (self.index + 1) % len(self.frames[self.direction])
				self.image = self.frames[self.direction][self.index]
			self.rect = self.rect.move(self.speed.x, self.speed.y)
			self.sprite_rect = self.sprite_rect.move(self.speed.x, self.speed.y)
			if self.rect.right > SCREEN_WIDTH - self.width:
				self.rect.left = self.width
				self.sprite_rect.left = self.width
			elif self.rect.left < self.width:
				self.rect.right = SCREEN_WIDTH - self.width
				self.sprite_rect.right = SCREEN_WIDTH - self.width
			elif self.rect.top < self.height:
				self.rect.bottom = SCREEN_HEIGHT - self.height
				self.sprite_rect.bottom = SCREEN_HEIGHT - self.height
			elif self.rect.bottom > SCREEN_HEIGHT - self.height:
				self.rect.top = self.height
				self.sprite_rect.top = self.height
		else:
			self.index = 0
			self.image = self.frames[self.direction][self.index]
		pass
	
	def move(self, position):
		self.rect = self.rect.move(position[0], position[1])
		if self.rect.right > SCREEN_WIDTH - self.width:
			self.rect.left = self.width
		elif self.rect.left < self.width:
			self.rect.right = SCREEN_WIDTH - self.width
		elif self.rect.top < self.height:
			self.rect.bottom = SCREEN_HEIGHT - self.height
		elif self.rect.bottom > SCREEN_HEIGHT - self.height:
			self.rect.top = self.height
	
	def find_path(self, end):
		start = self.grid_position
		came_from, cost_so_far = pathfinding.a_star(self.tilemap, start, end)
		self.path = pathfinding.reconstruct_path(came_from, start, end)


def spawn_entity(level, type_, id_):
	entity = Entity(str(type_), level.tilemap, id_)
	return entity
