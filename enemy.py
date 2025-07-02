# enemy.py

import pygame, os
from config import ENEMY_SIZE, ENEMY_TYPES

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, e_type):
        super().__init__()
        self.speed = e_type["speed"]
        self.hp = e_type["health"]
        path = os.path.join(os.path.dirname(__file__), e_type["img"])
        img = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(img, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect(midtop=(x,0))

    def update(self):
        self.rect.y += self.speed

    def take_damage(self,d):
        self.hp-=d
        return self.hp<=0
