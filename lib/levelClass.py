import pygame
from pygame.locals import *

from . import *


class Level:
	def __init__(self, position, dungeon="overworld"):
		self.grid_size = self.grid_width, self.grid_height = SCREEN_WIDTH/GRIDENTITY_WIDTH, SCREEN_HEIGHT/GRIDENTITY_HEIGHT
		self.grid = []
		self.layers = [[],[]]
		self.level_entities_to_spawn = {}
		self.level_entities = []
		path_to_lvl = PATH+LEVEL_FOLDER+CURRENT_CAMPAIN+"/"+dungeon+"/"+"{}-{}".format(position[0], position[1])+'.txt'
		with open(path_to_lvl, "r") as level:
			for line in level:
				if not "#" in line:
					to_append_to_grid = []
					line2 = line.split()
					for x in line2:
						if not "(" in x:
							to_append_to_grid.append(int(x))
							self.layers[0].append(1)
							self.layers[1].append(int(x))
						else:
							x = x[1:-1].split(",")
							for i in range(len(x)):
								self.layers[i].append(int(x[i]))
							to_append_to_grid.append(int(x[1]))
					self.grid.append(to_append_to_grid)
				else:
					line = line[1:].split(":")
					coords = line[1][:-1].split(";")
					self.level_entities_to_spawn[line[0]] = (int(coords[0]), int(coords[1]))
		self.gridentities = load_all("config/gridentities.yaml")
		self.drawn_gridentities= []
		self.tilemap = pathfinding.GridWithWeights(self.grid_width, self.grid_height)
		self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.get_drawn_entities()
		self.spawn_entities()

	def get_drawn_entities(self):
		num = 0
		print(self.grid)
		for y in range(len(self.grid)):
			line = self.grid[y]
			for x in range(len(line)):
				entity = line[x]
				ge = GridEntity(self.gridentities[entity], x, y, num)
				self.drawn_gridentities.append(ge)
				if not ge.can_pass:
					self.tilemap.walls.append((x, y))
				self.tilemap.weights[(x, y)] = ge.weight
				num += 1
	def draw(self):
		for grid_entity in self.drawn_gridentities:
			if grid_entity.has_been_updated:
				if grid_entity.is_transparent:
					to_blit_under = GridEntity(self.gridentities[self.layers[0][grid_entity.pos_on_grid]], grid_entity.x, grid_entity.y, grid_entity.pos_on_grid)
					if gridEntitiesGroupBlocking.has(to_blit_under):
						gridEntitiesGroupBlocking.remove(to_blit_under)
					self.surface.blit(to_blit_under.image, (grid_entity.x*GRIDENTITY_WIDTH, grid_entity.y*GRIDENTITY_HEIGHT))
				self.surface.blit(grid_entity.image, (grid_entity.x*GRIDENTITY_WIDTH, grid_entity.y*GRIDENTITY_HEIGHT))
				grid_entity.has_been_updated = False
	def get_grid_entity(self, pos):
		x=pos[0]
		y=pos[1]
		return self.drawn_gridentities[self.grid[y][x]]

	def spawn_entities(self):
		id_ = 0
		for key, value in self.level_entities_to_spawn.items():
			e = spawn_entity(self, key, id_)
			e.move(value)
			self.level_entities.append(e)
			id_ += 1
