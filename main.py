# -*- coding: utf-8 -*-

#import pygame
#import time
import sys
import random

import plane

#from plane import MyPlane
from textAndbutton import *

window_width = 480
window_height = 680
BULLETEVENT = pygame.USEREVENT +1
pygame.time.set_timer(BULLETEVENT, 250)

def key_control(hero_temp):
    for event in pygame.event.get():
        #print('key_control event type', event.type)
        if event.type == pygame.QUIT:
            print('key control exit')
            pygame.quit()
            sys.exit()
        elif event.type == BULLETEVENT:
            hero_temp.fire() # fire bullet by timer per 250ms
            # print('key_control')
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_temp.move_left()
    elif keys[pygame.K_RIGHT]:
        hero_temp.move_right()
    elif keys[pygame.K_UP]:
        hero_temp.move_up()
    elif keys[pygame.K_DOWN]:
        hero_temp.move_down()

def button_control(screen):
    # draw start button and exit button
    start_rect = MyRect(green, 70, 480, 130, 60)
    exit_rect = MyRect(red, 280, 480, 130, 60)
    start_text = Mytext("START", 135, 510, height = 35, color = white)
    exit_text = Mytext("EXIT", 345, 510, height = 35, color = white)
    
    # button color and function
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (70<=mouse[0]<=200 and 480<=mouse[1]<=540):
        start_rect.color = bright_green
        start_text.color = black
        if (click[0] == 1): # start game when click start button
            return False
      
    if (280<=mouse[0]<=410 and 480<=mouse[1]<=540):
        exit_rect.color = bright_red
        exit_text.color = black
        if (click[0] == 1): # exit game when click exit button
            pygame.quit()
            sys.exit()
    
    # draw button and text      
    start_rect.draw_button(screen)
    exit_rect.draw_button(screen)
    start_text.draw_text(screen)
    exit_text.draw_text(screen)

def start_game_info():
    screen = pygame.display.set_mode((window_width, window_height), 0, 32)
    backgroud = pygame.image.load('picture/bg.png')
    pygame.display.set_caption('Plane War')
    text_welcome1 = Mytext("Welcome to", window_width/2, window_height/3, height = 50, color = white)
    text_welcome2 = Mytext("Plane War!", window_width/2, window_height/2, height = 50, color = white)
    
    game_info = True
    
    while game_info:
        screen.blit(backgroud, (0, 0))
        text_welcome1.draw_text(screen)
        text_welcome2.draw_text(screen)
        if False == button_control(screen):
            game_info = False
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('game info exit')
                pygame.quit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    game_info = False
                    print(game_info)
                    break
    
def game_loop():
    game_on = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 680), 0, 32)
    background = pygame.image.load('picture/background.png')
    myplane = plane.MyPlane(screen)
    
    # 绘制障碍物
    enemy = plane.Enemy(screen)
    y = 0
    
    while game_on:
        screen.blit(background, (0, 0))
        '''
        for event in pygame.event.get():
            if event.type == BULLETEVENT:
                myplane.fire()
            elif event.type == pygame.QUIT:
                print('game on exit')
                pygame.quit()
                sys.exit()
        '''
        key_control(myplane)
        #print("tick is %d", pygame.time.get_ticks())
        
        myplane.display()
        enemy.display()
        if y>=0:
            y=y-5
        else :
            y = 680
        
        #pygame.draw.rect(screen, random.choice(mycolor), (random.randint(0,480), y,60,50))
        
        
        pygame.display.update()
        clock.tick(60) # 控制游戏运行帧率，没秒60帧

def main():
    pygame.init()
    pygame.mixer.init()
    start_game_info()
    game_loop()

if __name__ == "__main__":
    main()
    
    