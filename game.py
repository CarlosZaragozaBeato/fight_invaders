import pygame, sys 

from player import Player



screen_w = 1280
screen_h = 960

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("FIGHT INVADERS")


bg_color = pygame.Color("grey12")
clock = pygame.time.Clock()


player = Player(screen_h=screen_h, screen_w=screen_w)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_speed_x -= 20
            if event.key == pygame.K_RIGHT:
                player.player_speed_x += 20
            if event.key == pygame.K_UP:
                player.player_speed_y -= 20
            if event.key == pygame.K_DOWN:
                player.player_speed_y += 20
            
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.player_speed_x += 20
            if event.key == pygame.K_RIGHT:
                player.player_speed_x -= 20
            if event.key == pygame.K_UP:
                player.player_speed_y += 20
            if event.key == pygame.K_DOWN:
                player.player_speed_y -= 20
            

    # RESET COLORS
    screen.fill(bg_color)

    player.move_actions()


    pygame.draw.rect(screen, player.color, player.rect)
    pygame.display.flip()
    clock.tick(60)    




