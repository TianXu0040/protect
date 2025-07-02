# enemy.py

import pygame, random, os
from config import ENEMY_SIZE, ENEMY_SPEED, ENEMY_HEALTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        path = os.path.join(os.path.dirname(__file__), "enemy.png")
        img = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(img, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect=self.image.get_rect(midtop=(x,0))
        self.hp=ENEMY_HEALTH

    def update(self):
        self.rect.y+=ENEMY_SPEED

    def take_damage(self,d):
        self.hp-=d
        return self.hp<=0
