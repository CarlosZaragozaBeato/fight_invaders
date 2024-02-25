import pygame, sys 

from player import Player



screen_w = 1280
screen_h = 960

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("FIGHT INVADERS")


bg_color = pygame.Color("grey12")


clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # RESET COLORS
    screen.fill(bg_color)



    pygame.display.flip()
    clock.tick(60)    




