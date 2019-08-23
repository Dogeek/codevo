import pygame
from pygame.locals import *
from pymunk.vec2d import Vec2d as Vector2

from . import *
"""
from .constants import *
from .functions import *
"""
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, playerGroup, entitiesGroup)
		self.speed = Vector2(0, 0)
		self.index = 0
		self.direction = DOWN
		self.current_frame = 0
		self.MoveSpeed = 7
		self.level_position = (1, 1)
		self.level_has_changed = True
		self.level_name = "overworld"
		self.init_from_file()

	def init_from_file(self):
		data = load('config/player.yaml')
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
		self.rect = pygame.Rect(t, (self.sprite_rect.w-7, int(self.sprite_rect.h/2)-2))
		self.inventory = data["inventory"]
		self.mask = pygame.mask.from_surface(self.image)
		pass

	def update(self):
		if self.speed != Vector2(0,0):
			self.current_frame += 1
			if self.current_frame % self.frame_time == 0:
				self.index = (self.index + 1) % len(self.frames[self.direction])
				self.image = self.frames[self.direction][self.index]
			self.rect = self.rect.move(self.speed.x, self.speed.y)
			self.sprite_rect = self.sprite_rect.move(self.speed.x, self.speed.y)
			if self.rect.right > SCREEN_WIDTH:
				self.rect.left = self.width
				self.sprite_rect.left = self.width
				self.level_position = (self.level_position[0]+1, self.level_position[1])
				self.level_has_changed = True
			elif self.rect.left < 0:
				self.rect.right = SCREEN_WIDTH - self.width
				self.sprite_rect.right = SCREEN_WIDTH - self.width
				self.level_position = (self.level_position[0]-1, self.level_position[1])
				self.level_has_changed = True
			elif self.rect.top < 0:
				self.rect.bottom = SCREEN_HEIGHT - self.height
				self.sprite_rect.bottom = SCREEN_HEIGHT - self.height
				self.level_position = (self.level_position[0], self.level_position[1]-1)
				self.level_has_changed = True
			elif self.rect.bottom > SCREEN_HEIGHT:
				self.rect.top = self.height
				self.sprite_rect.top = self.height
				self.level_position = (self.level_position[0], self.level_position[1]+1)
				self.level_has_changed = True
		else:
			self.index = 0
			self.image = self.frames[self.direction][self.index]
		pass

	def handle_keypress(self, event):
		speed = [0, 0]
		blocking_grid_collision = pygame.sprite.spritecollide(self, gridEntitiesGroupBlocking, False)
		collision_sides = get_collision_side(self, blocking_grid_collision)
		if event.type == KEYDOWN:
			if event.key == K_UP and UP not in collision_sides:
				self.direction = UP
				speed[1] -= self.MoveSpeed
			elif event.key == K_DOWN and DOWN not in collision_sides:
				self.direction = DOWN
				speed[1] += self.MoveSpeed
			elif event.key == K_LEFT and LEFT not in collision_sides:
				self.direction = LEFT
				speed[0] -= self.MoveSpeed
			elif event.key == K_RIGHT and RIGHT not in collision_sides:
				self.direction = RIGHT
				speed[0] += self.MoveSpeed
		self.speed = Vector2(tuple(speed))
		pass

	def move(self, speed):
		self.speed = speed
		self.rect = self.rect.move(speed.x, speed.y)
		if self.rect.right > SCREEN_WIDTH - self.width:
			self.rect.left = self.width
		elif self.rect.left < self.width:
			self.rect.right = SCREEN_WIDTH - self.width
		elif self.rect.top < self.height:
			self.rect.bottom = SCREEN_HEIGHT - self.height
		elif self.rect.bottom > SCREEN_HEIGHT - self.height:
			self.rect.top = self.height
