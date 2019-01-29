import pygame


class MyPlane(object):
    def __init__(self, screen_temp):
        self.width = 100
        self.height = 124
        self.x = 190
        self.y = 520
        self.screen = screen_temp
        self.image = pygame.image.load('picture/hero.gif')
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def move_left(self):
        if self.x >= 0 :
            self.x -= 5
        
    def move_right(self):
        if self.x <= 385 :
            self.x += 5
            
    def move_up(self):
        if self.y >= 0 :
            self.y -= 5
        
    def move_down(self):
        if self.y <= 555 :
            self.y += 5
        
        