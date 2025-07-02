# main.py

import pygame, sys, random, math, os
import pygame_gui, pygame_shaders, particlepy
from particlepy.particle import Particle
from particlepy.shape import Rect

from config import *
from enemy import Enemy, BossEnemy
from turret import Turret
from menu import Menu
from powerup import PowerUp
from character_select import CharacterSelect
from leaderboard import save_score, get_leaderboard
from achievements import load_unlocked, save_unlocked, check_achievements
from achievement_screen import AchievementScreen

# 全局粒子系统
particle_system = particlepy.particle.ParticleSystem()

def show_health_advice(screen):
    clock=pygame.time.Clock()
    fonts=["SimHei","Microsoft YaHei","Arial"]
    tf=pygame.font.SysFont(fonts,HEALTH_ADVICE_TITLE_SIZE)
    xf=pygame.font.SysFont(fonts,HEALTH_ADVICE_TEXT_SIZE)
    while True:
        screen.fill(BLACK)
        t=tf.render(HEALTH_ADVICE_TITLE,True,WHITE)
        screen.blit(t,((SCREEN_WIDTH-t.get_width())//2,SCREEN_HEIGHT//6))
        for i,msg in enumerate(HEALTH_ADVICE_MESSAGES):
            s=xf.render(msg,True,WHITE)
            screen.blit(s,((SCREEN_WIDTH-s.get_width())//2,SCREEN_HEIGHT//6+60+i*40))
        p=xf.render("按任意键进入背景故事",True,WHITE)
        screen.blit(p,((SCREEN_WIDTH-p.get_width())//2,SCREEN_HEIGHT-100))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN: return
        clock.tick(30)

def show_story(screen):
    clock=pygame.time.Clock()
    fonts=["SimHei","Microsoft YaHei","Arial"]
    tf=pygame.font.SysFont(fonts,48)
    xf=pygame.font.SysFont(fonts,24)
    story=[
        "万年前，仙居遗迹浮现云端，",
        "传说其中蕴藏无穷仙力，",
        "三位守护者并肩而立，",
        "抵御魔族，守护净土。"
    ]
    while True:
        screen.fill(BLACK)
        t=tf.render("背景故事",True,WHITE)
        screen.blit(t,((SCREEN_WIDTH-t.get_width())//2,50))
        for i,l in enumerate(story):
            s=xf.render(l,True,WHITE)
            screen.blit(s,(50,120+i*30))
        p=xf.render("按任意键进入主菜单",True,WHITE)
        screen.blit(p,((SCREEN_WIDTH-p.get_width())//2,SCREEN_HEIGHT-100))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN: return
        clock.tick(30)

def show_help(screen):
    clock=pygame.time.Clock()
    fonts=["SimHei","Microsoft YaHei","Arial"]
    f=pygame.font.SysFont(fonts,32)
    lines=[
        "A/D 移动炮塔", "←/→ 调整角度", "空格 发射子弹",
        "拾取道具提升能力" ]
    while True:
        screen.fill(BLACK)
        screen.blit(f.render("游戏说明",True,WHITE),((SCREEN_WIDTH-200)//2,80))
        for i,l in enumerate(lines):
            t=f.render(l,True,WHITE)
            screen.blit(t,(80,160+i*40))
        p=f.render("按任意键返回",True,WHITE)
        screen.blit(p,((SCREEN_WIDTH-p.get_width())//2,SCREEN_HEIGHT-100))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN: return
        clock.tick(30)

def show_game_over(screen,kills):
    clock=pygame.time.Clock()
    fonts=["SimHei","Microsoft YaHei","Arial"]
    f=pygame.font.SysFont(fonts,36)
    name=""
    while True:
        screen.fill(BLACK)
        screen.blit(f.render("游戏结束",True,WHITE),((SCREEN_WIDTH-200)//2,100))
        screen.blit(f.render(f"击杀: {kills}",True,WHITE),((SCREEN_WIDTH-200)//2,150))
        instr=f.render("输入昵称并回车",True,WHITE)
        screen.blit(instr,((SCREEN_WIDTH-instr.get_width())//2,250))
        screen.blit(f.render(name,True,WHITE),((SCREEN_WIDTH-f.size(name)[0])//2,300))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_BACKSPACE: name=name[:-1]
                elif e.key==pygame.K_RETURN and name.strip():
                    save_score(name.strip(),kills)
                    return show_leaderboard(screen)
                elif e.unicode.isprintable(): name+=e.unicode
        clock.tick(30)

def show_leaderboard(screen):
    clock=pygame.time.Clock()
    fonts=["SimHei","Microsoft YaHei","Arial"]
    tf=pygame.font.SysFont(fonts,48)
    f=pygame.font.SysFont(fonts,36)
    lb=get_leaderboard()
    opts=["再来一次","回主菜单"];sel=0
    while True:
        screen.fill(BLACK)
        screen.blit(tf.render("排行榜",True,WHITE),((SCREEN_WIDTH-200)//2,50))
        for i,ent in enumerate(lb):
            screen.blit(f.render(f"{i+1}.{ent['name']} {ent['score']}",True,WHITE),(100,120+i*40))
        for i,o in enumerate(opts):
            pre="> " if i==sel else "  "
            color=HIGHLIGHT_COLOR if i==sel else WHITE
            screen.blit(f.render(pre+o,True,color),((SCREEN_WIDTH-200)//2,SCREEN_HEIGHT-150+i*40))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_UP: sel=(sel-1)%2
                if e.key==pygame.K_DOWN: sel=(sel+1)%2
                if e.key==pygame.K_RETURN: return "restart" if sel==0 else "menu"
        clock.tick(30)

def show_victory(screen, kills):
    clock = pygame.time.Clock()
    fonts = ["SimHei", "Microsoft YaHei", "Arial"]
    f = pygame.font.SysFont(fonts, 36)
    name = ""
    while True:
        screen.fill(BLACK)
        screen.blit(f.render("胜 利", True, WHITE), ((SCREEN_WIDTH-200)//2, 100))
        screen.blit(f.render(f"击杀: {kills}", True, WHITE), ((SCREEN_WIDTH-200)//2, 150))
        instr = f.render("输入昵称并回车", True, WHITE)
        screen.blit(instr, ((SCREEN_WIDTH-instr.get_width())//2, 250))
        screen.blit(f.render(name, True, WHITE), ((SCREEN_WIDTH-f.size(name)[0])//2, 300))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif e.key == pygame.K_RETURN and name.strip():
                    save_score(name.strip(), kills)
                    return show_leaderboard(screen)
                elif e.unicode.isprintable():
                    name += e.unicode
        clock.tick(30)

def run_game(character):
    # 切入 OpenGL 模式
    pygame.display.quit(); pygame.display.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.OPENGL|pygame.DOUBLEBUF)
    pygame.display.set_caption(GAME_TITLE)
    display_surf=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))

    # UI & Shader
    theme=os.path.join(os.path.dirname(__file__),"theme.json")
    ui_mgr=pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_HEIGHT),theme)
    health=pygame_gui.elements.UIStatusBar(pygame.Rect(10,10,200,25),manager=ui_mgr)
    shader=pygame_shaders.DefaultScreenShader(display_surf)
    kill_font=pygame.font.SysFont(["SimHei","Microsoft YaHei","Arial"],24)

    enemies=pygame.sprite.Group(); projs=pygame.sprite.Group(); powerups=pygame.sprite.Group(); boss_group=pygame.sprite.Group()
    boss_spawned = False
    boss_defeated = False
    # 成就数据
    ach_path = os.path.join(os.path.dirname(__file__), ACHIEVEMENT_FILE)
    unlocked = load_unlocked(ach_path)
    # Draw everything on the off-screen surface so the shader can process it
    turret = Turret(display_surf, enemies, projs,
                  character["fire_delay"],character["damage"],character["piercing"],
                  character["turret_img"],character["bullet_img"])
    clock=pygame.time.Clock(); prev=pygame.time.get_ticks()
    kills=0;hp=PLAYER_HEALTH
    pygame.time.set_timer(pygame.USEREVENT+1,ENEMY_SPAWN_DELAY)
    pygame.time.set_timer(pygame.USEREVENT+2,POWERUP_SPAWN_DELAY)

    running=True
    while running:
        now=pygame.time.get_ticks(); dt=(now-prev)/1000.0; prev=now
        particle_system.update(delta_time=dt)
        for e in pygame.event.get():
            if e.type==pygame.QUIT: return "menu"
            ui_mgr.process_events(e)
            if e.type==pygame.USEREVENT+1:
                et=random.choice(ENEMY_TYPES)
                enemies.add(Enemy(random.randint(ENEMY_SIZE//2,SCREEN_WIDTH-ENEMY_SIZE//2),et))
            if e.type==pygame.USEREVENT+2:
                pt=random.choice(POWERUP_TYPES)
                powerups.add(PowerUp(random.randint(20,SCREEN_WIDTH-20),pt))
        # 更新
        turret.update(); enemies.update(); boss_group.update(); projs.update(); powerups.update()
        # spawn boss
        if kills >= BOSS_SPAWN_KILLS and not boss_spawned:
            boss_group.add(BossEnemy(SCREEN_WIDTH//2, -BOSS_SIZE))
            boss_spawned = True
        # 敌人到底部
        for en in list(enemies):
            if en.rect.top>SCREEN_HEIGHT:
                pos=en.rect.center; en.kill(); hp-=1
                # 粒子爆炸
                for _ in range(20):
                    particle_system.emit(Particle(
                        shape=Rect(radius=5,angle=random.randint(0,360),color=(255,80,30),alpha=255),
                        position=pos,
                        velocity=(random.uniform(-100,100),random.uniform(-100,100)),
                        delta_radius=-0.2
                    ))
                if hp<=0: running=False
        for boss in list(boss_group):
            if boss.rect.top > SCREEN_HEIGHT:
                running = False
        # 碰撞
        cols=pygame.sprite.groupcollide(enemies,projs,False,False)
        for en,ps in cols.items():
            for p in ps:
                if en.take_damage(p.damage):
                    pos=en.rect.center; en.kill(); kills+=1
                    new_achs = check_achievements(kills, unlocked)
                    for a in new_achs:
                        print('Unlocked:', a)
                    for _ in range(30):
                        particle_system.emit(Particle(
                            shape=Rect(radius=5,angle=random.randint(0,360),color=(255,180,50),alpha=255),
                            position=pos,
                            velocity=(random.uniform(-200,200),random.uniform(-200,200)),
                            delta_radius=-0.3
                        ))
                if not p.piercing: p.kill()

        # Boss collision
        bcols = pygame.sprite.groupcollide(boss_group, projs, False, False)
        for boss, ps in bcols.items():
            for p in ps:
                if boss.take_damage(p.damage):
                    boss.kill(); boss_defeated = True; running = False
                if not p.piercing:
                    p.kill()
        # Power-up collision
        for pu in list(powerups):
            if turret.rect.colliderect(pu.rect):
                if pu.effect=="heal" and hp<PLAYER_HEALTH:
                    hp=min(PLAYER_HEALTH,hp+1)
                if pu.effect=="rapid":
                    turret.delay=max(100,int(turret.delay*0.7))
                if pu.effect=="piercing":
                    turret.piercing=True
                pu.kill()

        # 绘制
        display_surf.fill(WHITE)
        enemies.draw(display_surf); boss_group.draw(display_surf); projs.draw(display_surf); powerups.draw(display_surf)
        turret.draw()
        particle_system.render(surface=display_surf)
        health.percent_full=max(0.0,min(1.0,hp/PLAYER_HEALTH))
        kill_surf=kill_font.render(f"击杀: {kills}",True,BLACK)
        display_surf.blit(kill_surf,(SCREEN_WIDTH-kill_surf.get_width()-10,10))
        if boss_group:
            boss = boss_group.sprites()[0]
            hp_ratio = max(0, boss.hp / BOSS_HEALTH)
            bar_rect = pygame.Rect(SCREEN_WIDTH//2-100, 40, 200, 15)
            pygame.draw.rect(display_surf, (80,80,80), bar_rect)
            pygame.draw.rect(display_surf, (255,0,0), (bar_rect.x, bar_rect.y, int(bar_rect.width*hp_ratio), bar_rect.height))
        ui_mgr.update(dt); ui_mgr.draw_ui(display_surf)
        shader.render(); pygame.display.flip()
        clock.tick(FPS)

    # Switch back to a normal display for the game over and leaderboard screens
    pygame.display.quit(); pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    save_unlocked(ach_path, unlocked)
    if boss_defeated:
        return show_victory(screen, kills)
    else:
        return show_game_over(screen, kills)

def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    show_health_advice(screen); show_story(screen)
    menu=Menu(screen); clock=pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            c=menu.handle_event(e)
            if c=="开始游戏":
                char=CharacterSelect(screen).run()
                action=run_game(char)
                # 切回普通并重新创建菜单以更新屏幕引用
                pygame.display.quit();pygame.display.init()
                screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                pygame.display.set_caption(GAME_TITLE)
                menu = Menu(screen)
                if action!="restart": break
            elif c=="帮助":
                show_help(screen)
            elif c=="成就":
                AchievementScreen(screen).run()
            elif c=="退出":
                pygame.quit();sys.exit()
        menu.draw(); clock.tick(30)

if __name__=="__main__":
    main()
