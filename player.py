import pygame 

class Player:

    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.color = (255, 64, 125)
        self.player_speed_x = 0
        self.player_speed_y = 0 
        self.rect = pygame.Rect(screen_w / 2, screen_h - 50, 50, 50) 


    def move_actions(self):
        self.rect.x += self.player_speed_x
        self.rect.y += self.player_speed_y 

        print(self.rect.top)


        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= self.screen_w:
            self.rect.right = self.screen_w
 

        if self.rect.bottom >= self.screen_h :
            self.rect.bottom = self.screen_h 

        if self.rect.top <= self.screen_h // 2:
            self.rect.top =  self.screen_h // 2
 
 
    
    def basic_shoot(self, type):
        pass 

    



class PlayerSkills:

    def __init__(self):
        pass 
    