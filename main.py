#! /usr/bin/python3
import sys
import os
import pygame
from pygame.locals import *
from pymunk.vec2d import Vec2d as Vector2
import yaml
import random as rd

from lib import *
"""
from lib.playerClass import Player
from lib.levelClass import Level
from lib.uiEntityClass import UiEntity
from lib.consoleClass import Console
from lib.constants import *
from lib.functions import *
"""
pygame.init()
pygame.key.set_repeat(REPEAT_DELAY, REPEAT_INTERVAL)

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((640, 480))
		self.player = Player()
		self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.level_position = (1, 1)
		self._redraw()
		self.ui = UiEntity(self.player)
		self.console_mode = False
		self.consoleUI = Console()
		self.framecount = 0

	def mainloop(self):
		self.framecount += 1
		if not self.console_mode:
			if self.player.level_has_changed:
				self.player.level_has_changed = False
				self.level_position = self.player.level_position
				self._redraw()
			gridEntitiesGroupUpdate.update()
			uiEntityGroup.update()
			self.level.draw()
			playerGroup.update()
			entitiesGroup.update()
			self.screen.blit(self.background, self.player.sprite_rect, self.player.sprite_rect)
			self.screen.blit(self.level.surface, (0, 0))
			for entity in self.level.level_entities:
				if self.framecount % 10 == 0:
					entity_speed = [0, 0]
					if not entity.path:
						x_dest = rd.randint(2, self.level.grid_width-2)
						y_dest = rd.randint(2, self.level.grid_width-2)
						while (x_dest, y_dest) in self.level.tilemap.walls or not self.level.tilemap.in_bounds((x_dest, y_dest)):
							x_dest = rd.randint(2, 20-2)
							y_dest = rd.randint(2, 15-2)
						entity.find_path((x_dest, y_dest))
					path_poss = [(entity.grid_position[0]+x, entity.grid_position[1]+y) for (x,y) in [(1,0), (-1,0), (0,1), (0,-1)]]
					next_ = entity.path.pop(0)
					move = (entity.grid_position[0]-next_[0], entity.grid_position[1]-next_[1])
					if move[1]>0:# and UP not in collision_sides:
						entity.direction = UP
						entity_speed[1] -= entity.MoveSpeed
					elif move[1]<0:# and DOWN not in collision_sides:
						entity.direction = DOWN
						entity_speed[1] += entity.MoveSpeed
					elif move[0]>0:# and LEFT not in collision_sides:
						entity.direction = LEFT
						entity_speed[0] -= entity.MoveSpeed
					elif move[0]<0:# and RIGHT not in collision_sides:
						entity.direction = RIGHT
						entity_speed[0] += entity.MoveSpeed
					entity.speed = Vector2(tuple(entity_speed))
				self.screen.blit(self.level.surface, entity.sprite_rect, entity.sprite_rect)
				self.screen.blit(entity.image, entity.sprite_rect)
			self.screen.blit(self.player.image, self.player.sprite_rect)
			self.screen.blit(self.ui.surface, (10, 10))
		else:
			self.consoleUI.render()
			self.screen.blit(self.consoleUI.surface, (0, 0))
		pygame.display.update()
		pygame.time.delay(100)

	def event_handler(self):
		for event in pygame.event.get():
			if not self.console_mode:
				self.player.handle_keypress(event)
			if event.type in (QUIT, KEYDOWN):
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.key == K_TAB:
					self.console_mode = not self.console_mode
				else:
					self.consoleUI.handle_event(event)
	def _redraw(self):
		self.level = Level(self.level_position)
		self.level.draw()

game = Game()
while True:
	game.mainloop()
	game.event_handler()
