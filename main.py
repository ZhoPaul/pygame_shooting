import pygame
#import time
import sys

import plane

#from plane import MyPlane
from textAndbutton import Mytext, white

window_width = 480
window_height = 680


def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_temp.move_left()
    elif keys[pygame.K_RIGHT]:
        hero_temp.move_right()
    elif keys[pygame.K_UP]:
        hero_temp.move_up()
    elif keys[pygame.K_DOWN]:
        hero_temp.move_down()

def start_game_info():
    screen = pygame.display.set_mode((window_width, window_height), 0, 32)
    backgroud = pygame.image.load('picture/bg.png')
    text_welcome = Mytext("Welcome", window_width/2, window_height/3, color = white)
    
    game_info = True
    
    while game_info:
        screen.blit(backgroud, (0, 0))
        text_welcome.draw_text(screen)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    game_info = False
                    print(game_info)
                    break
 

    
def game_loop():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 680), 0, 32)
    background = pygame.image.load('picture/background.png')
    myplane = plane.MyPlane(screen)
    game_on = True
    
    while game_on :
        screen.blit(background, (0, 0))
        
        key_control(myplane)
        myplane.display()
        
        pygame.display.update()
        #time.sleep(0.01)
        clock.tick(60)
               

def main():
    pygame.init()
    pygame.mixer.init()
    start_game_info()
    game_loop()

if __name__ =="__main__":
    main()
    
    