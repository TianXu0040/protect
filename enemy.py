# enemy.py

import pygame, random
from config import ENEMY_SIZE, ENEMY_SPEED, ENEMY_HEALTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image=pygame.Surface((ENEMY_SIZE,ENEMY_SIZE))
        self.image.fill((200,50,50))
        self.rect=self.image.get_rect(midtop=(x,0))
        self.hp=ENEMY_HEALTH

    def update(self):
        self.rect.y+=ENEMY_SPEED

    def take_damage(self,d):
        self.hp-=d
        return self.hp<=0
