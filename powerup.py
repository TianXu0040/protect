import pygame, os
from config import POWERUP_TYPES

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, info):
        super().__init__()
        path=os.path.join(os.path.dirname(__file__), info["img"])
        self.image=pygame.transform.scale(pygame.image.load(path).convert_alpha(), (20,20))
        self.rect=self.image.get_rect(center=(x,0))
        self.effect=info["effect"]
        self.speed=1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top>pygame.display.get_surface().get_height():
            self.kill()
