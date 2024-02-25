import pygame
import sys
import random


def player_limits():
    player.x += player_speed

    if player.left <= 0:
        player.left = 0

    if player.right >= screen_w:
        player.right = screen_w


# formas geométricas aleatorias
def gen_enemies():
    global actual, last_enemy_time, enemies
    current_time = pygame.time.get_ticks()

    for _ in range(actual):
        x_rand = random.randint(50, int(screen_w - 50))
        y_rand = random.randint(50, int(screen_h / 2))
        enemy = pygame.Rect(x_rand, y_rand, 50, 50)
        enemies.append(enemy)
        actual += 1
        last_enemy_time = current_time


def player_shot():
    shot = pygame.Rect(int(player.x), int(player.y) - 50, 10, 50)
    return shot


def shot_hitbox(enemies, shoot):
    for enemy in enemies[:]:
        if shoot.colliderect(enemy): 
            enemies.remove(enemy)
            return True
    return False


pygame.init()
clock = pygame.time.Clock()

# main window
screen_w = 1280
screen_h = 960
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("01-HITTT")

# colors

color_player = (255, 64, 125)
light_grey = (200, 200, 200)
cum_shot = (245, 245, 245)
bg_color = pygame.Color("grey12")

# players
player = pygame.Rect(screen_w / 2, screen_h - 50, 50, 50)


round = 1

limit = 5
actual = 1
player_speed = 0
enemies = []
last_enemy_time = pygame.time.get_ticks()

shoot = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed -= 20
            if event.key == pygame.K_RIGHT:
                player_speed += 20
            if event.key == 32:
                if shoot is None:
                    shoot = player_shot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed += 20
            if event.key == pygame.K_RIGHT:
                player_speed -= 20

    screen.fill(bg_color)

    player_limits()

    if len(enemies) == 0:
        gen_enemies()
        round += 1
        actual += 5

    if shoot is not None:
        if shoot.y < 0 or shot_hitbox(enemies, shoot):
            shoot = None
        else:
            pygame.draw.rect(screen, cum_shot, shoot)
            shoot.y -= 50

    for enemy in enemies:
        pygame.draw.rect(screen, light_grey, enemy)

    pygame.draw.rect(screen, color_player, player)
    pygame.display.flip()
    clock.tick(60)
