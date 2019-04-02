import pygame

class MyPlane(object):
    def __init__(self, screen):
        self.width = 100
        self.height = 124
        self.pos_x = 190
        self.pos_y = 520
        self.screen = screen
        self.image = pygame.image.load('picture/hero.gif')
        self.speed = 5
        
    def display(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
        
    def move_left(self):
        if self.pos_x >= 0 :
            self.pos_x -= self.speed
        
    def move_right(self):
        if self.pos_x <= 385 :
            self.pos_x += self.speed
            
    def move_up(self):
        if self.pos_y >= 0 :
            self.pos_y -= self.speed
        
    def move_down(self):
        if self.pos_y <= 555 :
            self.pos_y += self.speed



class Bullet(object):
    def __init__(self, screen, pos_x, pos_y):
        self.image = pygame.image.load('picture/bullet.png')
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y

    def display(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
            
        