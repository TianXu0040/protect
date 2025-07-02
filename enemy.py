# enemy.py

import pygame, os
from config import ENEMY_SIZE, ENEMY_TYPES, BOSS_SIZE, BOSS_SPEED, BOSS_HEALTH, BOSS_IMG

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


class BossEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        path = os.path.join(os.path.dirname(__file__), BOSS_IMG)
        img = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(img, (BOSS_SIZE, BOSS_SIZE))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BOSS_SPEED
        self.hp = BOSS_HEALTH

    def update(self):
        self.rect.y += self.speed

    def take_damage(self, d):
        self.hp -= d
        return self.hp <= 0
