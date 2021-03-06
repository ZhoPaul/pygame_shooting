# coding: utf-8

#import pygame
import time
import sys
import random

import plane

#from plane import MyPlane
from textAndbutton import *

window_width = 480
window_height = 680

BULLETEVENT = pygame.USEREVENT +1
pygame.time.set_timer(BULLETEVENT, 300)

def key_control(hero_temp, screen):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_temp.move_left()
    elif keys[pygame.K_RIGHT]:
        hero_temp.move_right()
    elif keys[pygame.K_UP]:
        hero_temp.move_up()
    elif keys[pygame.K_DOWN]:
        hero_temp.move_down()

    """
    eventlist = pygame.event.get(pygame.QUIT)
    print(eventlist)
    """
    #pygame.event.clear(pygame.QUIT)
    #pygame.event.clear(BULLETEVENT)
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            print('key control exit')
            pygame.quit()
            sys.exit()
        if BULLETEVENT == event.type:
            hero_temp.fire()
        if pygame.KEYDOWN == event.type:
            if pygame.K_SPACE == event.key:
                check_pause(screen)

    """
    if pygame.event.get(pygame.QUIT):
        print('key control exit')
        pygame.quit()
        sys.exit()
    if pygame.event.get(BULLETEVENT):
        pygame.event.clear()
        #print('BULLETEVENT')
        hero_temp.fire()
        """

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

def check_collide(plane_Tmp, block_Tmp, screen):
    if plane_Tmp.rect.colliderect(block_Tmp.rect):
        crash_text = Mytext("You Crashed", window_width/2, window_height/3, height = 50, color = black)
        crash_text.draw_text(screen)
        pygame.display.update()
        while True:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                return False
            for event in pygame.event.get():
                print(event)
                if pygame.QUIT == event.type:
                    print('key control exit')
                    pygame.quit()
                    sys.exit()
    return True    

def check_shoot(myplane, block):
    shootblock = False
    for bullet in myplane.bullet_list:
        #print('block is not shooted')
        #print(myplane.bulletNum, bullet.rect)
        #print(block.rect)
        if block.rect.colliderect(bullet.rect):
            shootblock = True
            block.rect.x=random.randint(0, 420)
            block.rect.y=0
            block.color = random.choice(mycolor)
            myplane.bullet_list.remove(bullet)
            myplane.bulletNum = myplane.bulletNum-1
            #x=x+1
            #print(x)
            #print('block is shooted')
            return True
        #print(myplane.bulletNum, bullet.rect)
        #print('block rect is:', block.rect)
            
    if False==shootblock:
        block.display()
        return False

def check_pause(screen):
    #if pygame.key.get_pressed()[pygame.K_SPACE]:
    pause_text = Mytext("Pause", window_width/2, window_height/3, height = 50, color = black)
    pause_text.draw_text(screen)
    pygame.display.update()
    pygame.time.wait(500)
    game_pause = True
    while game_pause:
        #print(pause)
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                print('pause exit')
                pygame.quit()
                sys.exit()
            if pygame.KEYDOWN == event.type:
                if pygame.K_SPACE == event.key:
                    game_pause = False
                    return
        """if pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.time.wait(500)
            return
        if pygame.event.get(pygame.QUIT):
            print('crashed game exit')
            break"""
    """pygame.quit()
    sys.exit()"""

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
                sys.exit()
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
    # show block
    block = plane.Block(screen)
    # show pointer
    x=0
    pointer = Mytext("POINT: "+ str(x), 70, 25, height = 30, color = black)
    while game_on:
        #print("tick is %d", pygame.time.get_ticks())
        screen.blit(background, (0, 0))
        pointer.draw_text(screen)
        key_control(myplane, screen)

        myplane.display()
        # check bullet
        if check_shoot(myplane, block):
            x=x+1
            pointer.info = 'POINT:'+str(x)
        #print(x)
        #block.display()
        #pygame.draw.rect(screen, random.choice(mycolor), (random.randint(0,480), y,60,50))
        #print(myplane.bulletNum)
        
        # check user
        game_on = check_collide(myplane, block, screen)

        #check_pause(screen)
        pygame.display.update()
        #print(clock.get_time())
        clock.tick(60) # control fps to 60 per sec
        #time.sleep(0.01)

def main():
    pygame.init()
    pygame.mixer.init()
    start_game_info()
    game_runing = True
    while game_runing:
        game_loop()
        pygame.time.wait(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('game_runing game exit')
                game_runing = False
                pygame.quit()

if __name__ == "__main__":
    main()

