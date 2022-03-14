from lists_and_dicts import *
from textures import *
import pygame


class Character():

    def __init__(self, cord_x, cord_y, health=100, jump_h=10, weapon='sword', speed=5, direction=1 ):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.health = health
        self.jump_h = jump_h
        self.weapon = weapon
        self.speed = speed
        self.direction = direction

    def jump(self):
        self.cord_y += self.jump_h

    def move(self):
        self.cord_x += self.speed * self.direction

    def hill(self, point):
        self.health += point
    
    def take_damage(self, enemy):
        enemy.health -= damage_dict[self.weapon]
    
    def is_died(self):
        return self.hp <= 0
    
    def change_weapon(self, wep):
        self.weapon = wep

    def draw(self, screen):
        srf = pygame.image.load(empt)
        rct = srf.get_rect()
        screen.blit(srf, rct)