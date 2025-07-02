# menu.py

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, MENU_OPTIONS, WHITE, HIGHLIGHT_COLOR

class Menu:
    def __init__(self,screen):
        self.screen=screen
        fonts=["SimHei","Microsoft YaHei","Arial"]
        self.font=pygame.font.SysFont(fonts,48)
        self.sel=0

    def draw(self):
        self.screen.fill((0,0,0))
        title=self.font.render(GAME_TITLE, True, WHITE)
        self.screen.blit(title,((SCREEN_WIDTH-title.get_width())//2,80))
        for i,opt in enumerate(MENU_OPTIONS):
            prefix = "> " if i == self.sel else "  "
            color = HIGHLIGHT_COLOR if i == self.sel else WHITE
            surf = self.font.render(prefix + opt, True, color)
            self.screen.blit(surf, ((SCREEN_WIDTH - surf.get_width()) // 2, 200 + i * 60))
        pygame.display.flip()

    def handle_event(self,e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP: self.sel=(self.sel-1)%len(MENU_OPTIONS)
            if e.key==pygame.K_DOWN: self.sel=(self.sel+1)%len(MENU_OPTIONS)
            if e.key==pygame.K_RETURN: return MENU_OPTIONS[self.sel]
        return None
