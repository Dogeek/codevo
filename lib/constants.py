import yaml
import os
import pygame

PATH = os.getcwd()+"/"
with open(PATH+"config/config.yaml", "r") as f:
	config_file = yaml.safe_load(f)
SCREEN_WIDTH = config_file["screen_width"]
SCREEN_HEIGHT = config_file["screen_height"]
REPEAT_INTERVAL = config_file["repeat_interval"]
REPEAT_DELAY = config_file["repeat_delay"]
LANGUAGE = config_file["language"]
GRIDENTITIES_FOLDER = config_file["grid_entities_folder"]
LEVEL_FOLDER = config_file["level_folder"]
CURRENT_CAMPAIN = config_file['current_campain']

DOWN = 0
RIGHT = 1
LEFT = 2
UP = 3

GRIDENTITY_WIDTH = 32
GRIDENTITY_HEIGHT = 32

playerGroup = pygame.sprite.GroupSingle()
entitiesGroup = pygame.sprite.RenderUpdates()
gridEntitiesGroup = pygame.sprite.RenderPlain()
gridEntitiesGroupUpdate = pygame.sprite.RenderUpdates()
gridEntitiesGroupBlocking = pygame.sprite.RenderPlain()
uiEntityGroup = pygame.sprite.GroupSingle()
