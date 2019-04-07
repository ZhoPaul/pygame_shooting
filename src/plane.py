import pygame
import random
#import textAndbutton

from textAndbutton import mycolor

class MyPlane(object):
    def __init__(self, screen):
        self.width = 100
        self.height = 124
        self.screen = screen
        self.image = pygame.image.load('picture/hero.gif')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_width()/2 - self.rect.width/2
        self.rect.y = self.screen.get_height() - self.rect.height*1.5
        self.speed = 5
        self.bulletNum = 0
        self.bullet_list = []
        
    def display(self):
        # 显示子弹
        for bullet in self.bullet_list:
            #print('bullet.pos_y is %d', bullet.pos_y)
            if bullet.rect.y < 0:
                self.bullet_list.remove(bullet)
                self.bulletNum = self.bulletNum-1
                continue
            bullet.display()
        # 显示飞机
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move_left(self):
        if self.rect.x >= 0 :
            self.rect.x -= self.speed
        
    def move_right(self):
        if self.rect.x <= self.screen.get_width()-self.rect.width:
            self.rect.x += self.speed
            
    def move_up(self):
        if self.rect.y >= 0 :
            self.rect.y -= self.speed
        
    def move_down(self):
        if self.rect.y <= self.screen.get_height() - self.rect.height:
            self.rect.y += self.speed
    
    def fire(self):
        #print('BULLETEVENT')
        if self.bulletNum < 6:
            temp_bullet = Bullet(self.screen, self.rect.x, self.rect.y)
            self.bullet_list.append(temp_bullet)
            self.bulletNum = self.bulletNum+1
        #print('self.bulletNum is %d', self.bullet_list.__len__())
            
class Bullet(object):
    def __init__(self, screen, pos_x, pos_y):
        self.image = pygame.image.load('picture/bullet_1.gif')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = pos_x+48
        self.rect.y = pos_y
        self.speed = 10

    def display(self):
        if self.rect.y >= 0:
            self.rect.y = self.rect.y - self.speed
        
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
            
class Block(object):
    def __init__(self, screen, pos_x=random.randint(0, 450), pos_y=0):
    #def __init__(self, screen, pos_x=100, pos_y=0):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 60
        self.height = 50
        self.speed = 4
        self.color = random.choice(mycolor)
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def display(self):
        #print("y and x:",self.pos_y,self.pos_x)
        if self.rect.y >= 0 and self.rect.y <= 680:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = 0
            self.rect.x = random.randint(0, 450)
            #self.rect.x = 100
            self.color = random.choice(mycolor)
        #tmprect = (self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        #显示彩色的砖块
        #pygame.draw.rect(self.screen, random.choice(mycolor), tmprect)
        #clock.tick(60)
