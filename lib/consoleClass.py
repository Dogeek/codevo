import pygame
from pygame.locals import *
import math

from . import *

class Console():
	def __init__(self):
		self.font = pygame.font.Font(None, 24)
		self.return_str = ""
		self.whole_text = ""
		self.text_to_blit = []
		self.color = (112, 226, 77)
		self.bgcolor = (0, 0, 0)
		self.input_prompt = self.font.render(">", False, self.color)
		self.surface = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH))
		self.surface.fill(self.bgcolor)
		self.commands = load("config/commands.yaml")

	def handle_event(self, event):
		mods = pygame.key.get_mods()
		if event.key in range(K_SPACE, K_BACKQUOTE+1):
			self.return_str += """ !"#$\&'()*+,-./0123456789:;<=>?@[\\]^_``"""[event.key-K_SPACE]
		if event.key in range(K_a, K_z+1):
			s = "abcdefghijklmnopqrstuvwxyz"
			if is_in_mask(KMOD_SHIFT, mods):
				s.upper()
			else:
				s.lower()
			self.return_str += s[event.key-K_a]
		if event.key in range(K_KP0, K_KP9+1):
			self.return_str += "0123456789"[event.key-K_KP0]
		if event.key == K_RETURN or event.key == K_KP_ENTER:
			self.text_to_blit.append(self.font.render(self.return_str, False, self.color))
			self.whole_text += self.return_str+"\n"
			self.return_str = ""
		if event.key == K_BACKSPACE:
			self.return_str = self.return_str[:-1]

	def render(self):
		self.surface = pygame.Surface((SCREEN_HEIGHT, SCREEN_WIDTH))
		h = self.font.size("w")[1]+1
		for i in range(len(self.text_to_blit)):
			self.surface.blit(self.input_prompt, (0, i*h))
			self.surface.blit(self.text_to_blit[i], (32, i*h))
		self.surface.blit(self.input_prompt, (0, len(self.text_to_blit)*h))
		self.surface.blit(self.font.render(self.return_str, False, self.color), (32, len(self.text_to_blit)*h))

	def parse(self, unlocks):
		for line in self.whole_text:
			for key in self.commands.keys():
				if key in line:
					print(self.commands[key]["description"])
