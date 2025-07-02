# turret.py

import pygame, math, random, os
from projectile import Projectile
from config import TURRET_RADIUS

class Turret(pygame.sprite.Sprite):
    def __init__(self, screen, enemies, projectiles,
                 fire_delay, damage, piercing,
                 turret_img, bullet_img):
        super().__init__()
        self.screen = screen
        self.enemies = enemies
        self.projectiles = projectiles
        self.delay = fire_delay
        self.damage = damage
        self.piercing = piercing
        self.bimg = bullet_img
        path = os.path.join(os.path.dirname(__file__), turret_img)
        base = pygame.image.load(path).convert_alpha()
        self.base = pygame.transform.scale(base, (TURRET_RADIUS * 2, TURRET_RADIUS * 2))
        self.image = self.base
        w,h=self.image.get_size()
        self.rect=self.image.get_rect(center=(screen.get_width()//2, screen.get_height()-50))
        self.angle=0
        self.last_fire=pygame.time.get_ticks()

    def update(self):
        # rotate
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle = (self.angle + 2) % 360
        if keys[pygame.K_RIGHT]:
            self.angle = (self.angle - 2) % 360
        # Rotate clockwise to match the bullet direction
        self.image = pygame.transform.rotate(self.base, -self.angle)
        self.rect=self.image.get_rect(center=self.rect.center)
        # fire
        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and now - self.last_fire >= self.delay:
            self.last_fire = now
            rad = math.radians(self.angle)
            dx, dy = math.sin(rad), -math.cos(rad)
            sx = self.rect.centerx + dx * TURRET_RADIUS
            sy = self.rect.centery + dy * TURRET_RADIUS
            proj = Projectile((sx, sy), self.angle, self.damage, self.piercing, self.bimg)
            self.projectiles.add(proj)

    def draw(self):
        self.screen.blit(self.image, self.rect)
