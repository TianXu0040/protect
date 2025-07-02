# config.py

import pygame

# === 屏幕 & 帧率 ===
SCREEN_WIDTH       = 800
SCREEN_HEIGHT      = 600
FPS                = 60

# === 颜色 ===
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
HIGHLIGHT_COLOR = (255, 215, 0)  # 金色，用于高亮选项

# === 炮塔 & 子弹默认配置 ===
TURRET_RADIUS         = 20
DEFAULT_FIRE_DELAY    = 500       # 毫秒
DEFAULT_BULLET_DAMAGE = 100

# === 敌人配置 ===
ENEMY_SIZE         = 30
ENEMY_SPAWN_DELAY  = 2000        # 毫秒
ENEMY_SPEED        = 1
ENEMY_HEALTH       = 100

# 多种敌人类型，可拓展游戏难度
ENEMY_TYPES = [
    {"speed": 1,   "health": 100, "img": "enemy.png"},   # 普通
    {"speed": 2,   "health": 70,  "img": "enemy.png"},   # 快速
    {"speed": 0.5, "health": 300, "img": "enemy.png"},   # 坚甲
]

# 随机掉落的道具
POWERUP_SPAWN_DELAY = 8000       # 毫秒
POWERUP_TYPES = [
    {"name": "heal",       "img": "bullet1.png", "effect": "heal"},
    {"name": "rapid",      "img": "bullet2.png", "effect": "rapid"},
    {"name": "piercing",   "img": "bullet3.png", "effect": "piercing"},
]

# === 菜单 & UI ===
MENU_OPTIONS       = ["开始游戏", "帮助", "成就", "退出"]

# === 健康忠告 ===
HEALTH_ADVICE_TITLE       = "健康游戏忠告"
HEALTH_ADVICE_MESSAGES    = [
    "抵制不良游戏，拒绝盗版游戏。",
    "注意自我保护，谨防受骗上当。",
    "适度游戏益脑，沉迷游戏伤身。",
    "合理安排时间，享受健康生活。"
]
HEALTH_ADVICE_TITLE_SIZE  = 60
HEALTH_ADVICE_TEXT_SIZE   = 36
HEALTH_ADVICE_LINE_GAP    = 10

# === 我方配置 ===
PLAYER_HEALTH      = 3

# === 排行榜 ===
LEADERBOARD_FILE        = "leaderboard.json"
LEADERBOARD_MAX_ENTRIES = 10

# === 成就存档 ===
ACHIEVEMENT_FILE = "unlocked.txt"

# === 游戏标题 ===
GAME_TITLE = "守护仙居"
