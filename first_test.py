#! /usr/bin/python3
import sys
import pygame
from pygame.locals import *

pygame.init()
class GameObject:
    def __init__(self, image, height, width, speedx, speedy):
        self.speedx = speedx
        self.speedy = speedy
        self.image = image
        self.pos = image.get_rect().move(width, height)
    def move(self):
        self.pos = self.pos.move(self.speedx, self.speedy)
        if self.pos.right > 600:
            self.pos.left = 0

screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('sprites/entities/angel.png').convert()
player.set_colorkey((255, 0, 0))
background = pygame.image.load('sprites/background.jpg').convert()
screen.blit(background, (0, 0))
o = GameObject(player, 32, 32, 0, 0)
speedValue = 2
repeat_interval = 10 #ms
repeat_delay = 20 #ms
pygame.key.set_repeat(repeat_delay, repeat_interval)
while 1:
    speed = [0, 0]
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            if event.type == QUIT or event.key == K_q:
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                speed[1] -= speedValue
            if event.key == K_DOWN:
                speed[1] += speedValue
            if event.key == K_LEFT:
                speed[0] -= speedValue
            if event.key == K_RIGHT:
                speed[0] += speedValue
    o.speedx = speed[0]
    o.speedy = speed[1]
    screen.blit(background, o.pos, o.pos)
    o.move()
    screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)
