import pygame
import random
#import textAndbutton

from textAndbutton import mycolor

class MyPlane(object):
    def __init__(self, screen):
        self.width = 100
        self.height = 124
        self.pos_x = 190
        self.pos_y = 520
        self.screen = screen
        self.image = pygame.image.load('picture/hero.gif')
        self.rect = self.image.get_rect()
        self.speed = 5
        self.bulletNum = 0
        self.bullet_list = []
        
    def display(self):
        # 显示子弹
        for bullet in self.bullet_list:
            #print('bullet.pos_y is %d', bullet.pos_y)
            if bullet.pos_y < 0:
                self.bullet_list.remove(bullet)
                self.bulletNum = self.bulletNum-1
                continue
            bullet.display()
        # 显示飞机
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
    
    def fire(self):
        #print('BULLETEVENT')
        if self.bulletNum < 5:
            temp_bullet = Bullet(self.screen, self.pos_x, self.pos_y)
            self.bullet_list.append(temp_bullet)
            self.bulletNum = self.bulletNum+1
        #print('self.bulletNum is %d', self.bulletNum)
            
class Bullet(object):
    def __init__(self, screen, pos_x, pos_y):
        self.image = pygame.image.load('picture/bullet_1.gif')
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 6

    def display(self):
        if self.pos_y >= 0:
            self.pos_y = self.pos_y - self.speed
        
        self.screen.blit(self.image, (self.pos_x+48, self.pos_y))
            
class Enemy(object):
    def __init__(self, screen, pos_x=0, pos_y=0):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 4
        self.color = random.choice(mycolor)
        #self.rect = (self.pos_x, self.pos_y, 60, 50)

    def display(self):
        #print("y and x:",self.pos_y,self.pos_x)
        if self.pos_y >= 0 and self.pos_y <= 680:
            self.pos_y = self.pos_y + self.speed
        else :
            self.pos_y = 0
            self.pos_x = random.randint(0, 450)
            self.color = random.choice(mycolor)
        tmprect = (self.pos_x, self.pos_y, 60, 50)
        pygame.draw.rect(self.screen, self.color, tmprect)
        
        #显示彩色的砖块
        #pygame.draw.rect(self.screen, random.choice(mycolor), tmprect)
        #clock.tick(60)
    
    
    
