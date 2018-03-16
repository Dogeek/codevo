#-*- encoding:utf8 -*-
#!/usr/bin/python3
"""
Level Editor for CodEvo by Dogeek
Copyright (c) 2017 Copyright Holder All Rights Reserved.
"""
import tkinter as tk
import os
import yaml

#Constants defined below
PATH = os.getcwd()+"/../"
with open(PATH+"config/config.yaml", "r") as f:
	config_file = yaml.safe_load(f)
SCREEN_WIDTH = config_file["screen_width"]
SCREEN_HEIGHT = config_file["screen_height"]
GRIDENTITIES_FOLDER = config_file["grid_entities_folder"]
LEVEL_FOLDER = config_file["level_folder"]
DOWN = 0
RIGHT = 1
LEFT = 2
UP = 3
GRIDENTITY_WIDTH = 32
GRIDENTITY_HEIGHT = 32

#Functions defined below
def load(filename):
	with open(PATH+filename, "r") as f:
		data = yaml.safe_load(f)
	return data

def load_all(filename):
	with open(PATH+filename, "r") as f:
		data = yaml.safe_load_all(f)
		data = [d for d in data]
	return data

#GUI class
class GUI(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(master)
		self.master = master
		self.canvas = tk.Canvas(self, width=self.winfo_width, height=self.winfo_height)
		self.menubar = tk.Menu()
