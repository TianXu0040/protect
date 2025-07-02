# projectile.py

import pygame, math, os
from config import DEFAULT_BULLET_DAMAGE

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, angle, damage, piercing, image_path):
        super().__init__()
        self.damage=damage
        self.piercing=piercing
        path = os.path.join(os.path.dirname(__file__), image_path)
        base = pygame.image.load(path).convert_alpha()
        base = pygame.transform.scale(base, (10, 10))
        # Rotate clockwise to align with the turret orientation
        self.image = pygame.transform.rotate(base, -angle)
        self.rect = self.image.get_rect(center=pos)
        # Projectile motion uses the same clockwise angle
        rad = math.radians(angle)
        self.vx, self.vy = math.sin(rad) * 5, -math.cos(rad) * 5

    def update(self):
        self.rect.x+=self.vx; self.rect.y+=self.vy
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()
