# character_select.py

import pygame, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_FIRE_DELAY, DEFAULT_BULLET_DAMAGE, MENU_OPTIONS, WHITE, HIGHLIGHT_COLOR
# （如果 MENU_FONT_* 未定义，可使用 SysFont）

CHARACTERS = [
    {
        "name": "铁灰大炮",
        "fire_delay": DEFAULT_FIRE_DELAY,
        "damage": DEFAULT_BULLET_DAMAGE,
        "piercing": False,
        "turret_img": "turret1.png",
        "bullet_img": "bullet1.png"
    },
    {
        "name": "森林弓弩",
        "fire_delay": DEFAULT_FIRE_DELAY * 2,
        "damage": 200,
        "piercing": True,
        "turret_img": "turret2.png",
        "bullet_img": "bullet2.png"
    },
    {
        "name": "快枪",
        "fire_delay": int(DEFAULT_FIRE_DELAY / 1.5),
        "damage": 50,
        "piercing": False,
        "turret_img": "turret3.png",
        "bullet_img": "bullet3.png"
    }
]

class CharacterSelect:
    def __init__(self, screen):
        self.screen = screen
        fonts = ["SimHei","Microsoft YaHei","Arial"]
        size = 48
        self.title_font = pygame.font.SysFont(fonts, size)
        self.option_font = pygame.font.SysFont(fonts, size)
        self.info_font = pygame.font.SysFont(fonts, int(size*0.6))
        self.selected = 0

    def draw(self):
        self.screen.fill((0,0,0))
        title = self.title_font.render("选择角色", True, WHITE)
        self.screen.blit(title, ((SCREEN_WIDTH-title.get_width())//2, 80))
        # options
        for i, c in enumerate(CHARACTERS):
            prefix = "> " if i == self.selected else "  "
            color = HIGHLIGHT_COLOR if i == self.selected else WHITE
            surf = self.option_font.render(prefix + c["name"], True, color)
            self.screen.blit(surf, ((SCREEN_WIDTH - surf.get_width()) // 2, 160 + i * 60))
        # info table
        c = CHARACTERS[self.selected]
        x0, y0 = SCREEN_WIDTH//2-150, 160+len(CHARACTERS)*60 + 20
        pygame.draw.rect(self.screen, (0,0,0), (x0,y0,300,120))
        pygame.draw.rect(self.screen, (255,255,255), (x0,y0,300,120),1)
        rows = [("威力",str(c["damage"])),("延迟",str(c["fire_delay"])),("穿透","是" if c["piercing"] else "否")]
        for i,(k,v) in enumerate(rows):
            self.screen.blit(self.info_font.render(k,True,(255,255,255)),(x0+10,y0+10+i*30))
            self.screen.blit(self.info_font.render(v,True,(255,255,255)),(x0+150,y0+10+i*30))
        pygame.display.flip()

    def run(self):
        clock=pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit();sys.exit()
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP: self.selected=(self.selected-1)%len(CHARACTERS)
                    if e.key==pygame.K_DOWN: self.selected=(self.selected+1)%len(CHARACTERS)
                    if e.key==pygame.K_RETURN: return CHARACTERS[self.selected]
            self.draw()
            clock.tick(30)
