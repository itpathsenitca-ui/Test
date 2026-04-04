import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Shooter EXTENDED")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 60, 60)
BLUE = (60, 120, 255)
GREEN = (60, 220, 60)
GRAY = (150, 150, 150)
YELLOW = (255, 220, 0)
PURPLE = (180, 80, 255)

font_big = pygame.font.SysFont(None, 72)
font_mid = pygame.font.SysFont(None, 48)
font_small = pygame.font.SysFont(None, 26)

MENU = "menu"
PLAY = "play"
PAUSE = "pause"
GAME_OVER = "game_over"
state = MENU

PLAYER_SIZE = 50
player_speed = 7
player_rect = pygame.Rect(WIDTH//2-PLAYER_SIZE//2, HEIGHT-100, PLAYER_SIZE, PLAYER_SIZE)

bullets = []
BULLET_SPEED = 11
SHOOT_DELAY = 300
last_shot = 0
auto_fire = False

enemies = []
enemy_speed = 3

# enemy = {"rect": Rect, "hp": int, "type": str}

explosions = []  # (x, y, timer)

bonuses = []  # (rect, type)

score = 0
kills = 0
lives = 3
level = 1
best_score = 0
start_time = 0

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 800)

def reset_game():
    global enemies, bullets, bonuses, explosions
    global score, kills, lives, level, enemy_speed, start_time, auto_fire
    enemies = []
    bullets = []
    bonuses = []
    explosions = []
    score = 0
    kills = 0
    lives = 3
    level = 1
    enemy_speed = 3
    auto_fire = False
    player_rect.centerx = WIDTH // 2
    start_time = time.time()

def draw_text_center(text, font, color, y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(WIDTH//2, y))
    screen.blit(img, rect)

def spawn_enemy():
    x = random.randint(0, WIDTH-50)
    enemy_type = random.choice(["normal", "tank"])
    hp = 1 if enemy_type == "normal" else 3
    enemies.append({
        "rect": pygame.Rect(x, -50, 50, 50),
        "hp": hp,
        "type": enemy_type
    })

def spawn_bonus(x, y):
    btype = random.choice(["life", "rapid"])
    rect = pygame.Rect(x, y, 30, 30)
    bonuses.append((rect, btype))

def draw_ui():
    texts = [
        f"Score: {score}",
        f"Lives: {lives}",
        f"Kills: {kills}",
        f"Level: {level}",
        f"AutoFire: {'ON' if auto_fire else 'OFF'}"
    ]
    for i, t in enumerate(texts):
        screen.blit(font_small.render(t, True, BLACK), (10, 10 + i*22))

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset_game()
                state = PLAY

        elif state == PLAY:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = PAUSE
                if event.key == pygame.K_f:
                    auto_fire = not auto_fire
                if event.key == pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    if now - last_shot > SHOOT_DELAY:
                        bullets.append(pygame.Rect(player_rect.centerx-3, player_rect.top, 6, 14))
                        last_shot = now

            if event.type == SPAWN_EVENT:
                spawn_enemy()

        elif state == PAUSE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = PLAY

        elif state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    state = PLAY
                if event.key == pygame.K_m:
                    state = MENU

    if state == PLAY:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        player_rect.x = max(0, min(WIDTH-PLAYER_SIZE, player_rect.x))

        if auto_fire:
            now = pygame.time.get_ticks()
            if now - last_shot > SHOOT_DELAY:
                bullets.append(pygame.Rect(player_rect.centerx-3, player_rect.top, 6, 14))
                last_shot = now

        for bullet in bullets[:]:
            bullet.y -= BULLET_SPEED
            if bullet.bottom < 0:
                bullets.remove(bullet)

        for enemy in enemies[:]:
            enemy["rect"].y += enemy_speed
            if enemy["rect"].top > HEIGHT:
                enemies.remove(enemy)
                lives -= 1

            for bullet in bullets[:]:
                if enemy["rect"].colliderect(bullet):
                    bullets.remove(bullet)
                    enemy["hp"] -= 1
                    if enemy["hp"] <= 0:
                        explosions.append([enemy["rect"].centerx, enemy["rect"].centery, 15])
                        if random.random() < 0.2:
                            spawn_bonus(enemy["rect"].x, enemy["rect"].y)
                        enemies.remove(enemy)
                        score += 5
                        kills += 1
                        if kills % 10 == 0:
                            level += 1
                            enemy_speed += 0.5
                    break

            if enemy["rect"].colliderect(player_rect):
                enemies.remove(enemy)
                lives -= 1

        for bonus in bonuses[:]:
            rect, btype = bonus
            rect.y += 3
            if rect.colliderect(player_rect):
                if btype == "life":
                    lives += 1
                if btype == "rapid":
                    SHOOT_DELAY = max(100, SHOOT_DELAY - 50)
                bonuses.remove(bonus)

        for exp in explosions[:]:
            exp[2] -= 1
            if exp[2] <= 0:
                explosions.remove(exp)

        if lives <= 0:
            best_score = max(best_score, score)
            state = GAME_OVER

    if state == MENU:
        draw_text_center("BLOCK SHOOTER", font_big, BLUE, 200)
        draw_text_center("SPACE - Start", font_mid, BLACK, 330)

    elif state == PLAY:
        pygame.draw.rect(screen, BLUE, player_rect)

        for bullet in bullets:
            pygame.draw.rect(screen, YELLOW, bullet)

        for enemy in enemies:
            color = RED if enemy["type"] == "normal" else PURPLE
            pygame.draw.rect(screen, color, enemy["rect"])

        for rect, btype in bonuses:
            pygame.draw.rect(screen, GREEN if btype == "life" else GRAY, rect)

        for x, y, t in explosions:
            pygame.draw.circle(screen, RED, (x, y), t)

        draw_ui()

    elif state == PAUSE:
        draw_text_center("PAUSED", font_big, BLACK, 300)

    elif state == GAME_OVER:
        draw_text_center("GAME OVER", font_big, RED, 250)
        draw_text_center(f"Score: {score}", font_mid, BLACK, 330)
        draw_text_center(f"Best: {best_score}", font_mid, BLACK, 380)
        draw_text_center("R - Restart | M - Menu", font_small, BLACK, 450)

    pygame.display.update()

pygame.quit()
sys.exit()
