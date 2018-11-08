#sprite classes for game

import pygame as pg 
from pygame.sprite import Sprite
import random
from settings import *


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.falling = False
        self.acceleration = 0.5
    def update(self):
        self.vx = 0
        self.vy = 0
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5
        if keys[pg.K_UP]:
            self.jump()
        
        self.rect.x += self.vx
        self.rect.y += self.vy

    def jump(self):
        #decelerate exponentially
        """for i in range(5):
            self.rect.y - i
        for i in range(5):
            self.rect.y + 1"""
        self.vy = -50
        print("Jump is running")
        self.rect.x += self.vx
        self.rect.y += self.vy
        #accelerate exponentially
    def gravity(self):
        if self.rect.y < HEIGHT-40:
            self.falling = True
            print("Gravity is happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        elif self.rect.y >= HEIGHT-1:
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT -40
            print("Gravity is not happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
        

        


class Enemy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.falling = False
        self.acceleration = 0.5
        
    def update(self):
        self.vx = 0
        self.vy = 0
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = -5
        if keys[pg.K_d]:
            self.vx = 5
        if keys[pg.K_w]:
            self.jump()
        self.rect.x += self.vx
        self.rect.y += self.vy

    def jump(self):
        #decelerate exponentially
        """for i in range(5):
            self.rect.y - i
        for i in range(5):
            self.rect.y + 1"""
        self.vy = -50
        print("Jump is running")
        #accelerate exponentially
        self.rect.x += self.vx
        self.rect.y += self.vy
    def gravity(self):
        if self.rect.y < HEIGHT-40:
            self.falling = True
            print("Gravity is happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        elif self.rect.y >= HEIGHT:
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT -40
            print("Gravity is not happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
        
 
class Platform(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((100,50))
        self.image.fill(IDK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0