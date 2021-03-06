# coding: utf-8
import pygame
#from pip._vendor.pyparsing import White

black = (0, 0, 0)
white = (255, 255, 255)
red = (180, 80, 80)
green = (89, 180, 111)
blue = (0, 100, 255)

bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

mycolor = [black, white, red, green, blue]

class Mytext(object):
    def __init__(self, info = "hello", pos_x = 0, pos_y = 0, height = 30, color = black, font = 'comicsansms'):
        self.info = info
        self.height = height
        self.pos = (pos_x, pos_y)
        self.font = font
        self.color = color
    """
    def set_textcolor(self, color):
        self.color = color
    """
    def draw_text(self, screen):
        fontobj = pygame.font.SysFont(self.font, self.height)
        text_surf = fontobj.render(self.info, True, self.color)
        text_rect = text_surf.get_rect()
        text_rect.center = self.pos
        screen.blit(text_surf, text_rect)

class MyRect(object):
    def __init__(self, color = red, x = 0, y = 0, width = 10, height = 10):      
        self.color = color
        self.rect = (x, y, width, height)
        
    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)    
        