import yaml
import pygame
from . import *

def load(filename):
	with open(PATH+filename, "r") as f:
		data = yaml.safe_load(f)
	return data

def load_all(filename):
	with open(PATH+filename, "r") as f:
		data = yaml.safe_load_all(f)
		data = [d for d in data]
	return data

def get_collision_side(sprite, collide_rects):
	sprite_rect = sprite.rect
	collision_sides = [20]
	if collide_rects:
		collide_rect = collide_rects[0].rect
		bot = pygame.Rect(sprite_rect.bottomleft, (sprite_rect.w, 2))
		top = pygame.Rect(sprite_rect.topleft, (sprite_rect.w, 2))
		right = pygame.Rect(sprite_rect.topright, (2, sprite_rect.h))
		left = pygame.Rect(sprite_rect.topleft, (2, sprite_rect.h))
		if collide_rect.colliderect(bot):
			collision_sides.append(DOWN)
		if collide_rect.colliderect(top):
			collision_sides.append(UP)
		if collide_rect.colliderect(left):
			collision_sides.append(LEFT)
		if collide_rect.colliderect(right):
			collision_sides.append(RIGHT)
	return collision_sides

def is_in_mask(smth, mask):
	return ((smth & mask) == mask)

def pos_to_grid(pos):
	x = pos.x
	y = pos.y
	x /= GRIDENTITY_WIDTH
	y /= GRIDENTITY_HEIGHT
	x = int(x)
	y = int(y)
	return x,y

def grid_to_pos(pos):
	x = pos.x*32
	y = pos.y*32
	return x, y



print("functions.py loaded successfully")
