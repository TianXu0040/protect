# achievement_screen.py

import pygame, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, HIGHLIGHT_COLOR
from achievements import ACHIEVEMENTS

class AchievementScreen:
    def __init__(self, screen):
        self.screen = screen
        fonts = ["SimHei","Microsoft YaHei","Arial"]
        self.font = pygame.font.SysFont(fonts, 36)
        self.title_font = pygame.font.SysFont(fonts, 48)
        self.index = 0
        self.page_size = 15

    def draw(self):
        self.screen.fill((0,0,0))
        title = self.title_font.render("成就列表", True, WHITE)
        self.screen.blit(title, ((SCREEN_WIDTH-title.get_width())//2, 50))
        start = self.index * self.page_size
        end = start + self.page_size
        for i, ach in enumerate(ACHIEVEMENTS[start:end], start=0):
            text = f"{ach['id']}. {ach['name']}"
            surf = self.font.render(text, True, WHITE)
            self.screen.blit(surf, (80, 140 + i * 30))
        note = self.font.render("上下翻页, ESC返回", True, HIGHLIGHT_COLOR)
        self.screen.blit(note, (80, SCREEN_HEIGHT-80))
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        return
                    if e.key in (pygame.K_UP, pygame.K_LEFT):
                        if self.index > 0:
                            self.index -= 1
                    if e.key in (pygame.K_DOWN, pygame.K_RIGHT):
                        if (self.index+1)*self.page_size < len(ACHIEVEMENTS):
                            self.index += 1
            self.draw()
            clock.tick(30)
