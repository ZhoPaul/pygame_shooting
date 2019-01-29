import pygame
import time

from plane import MyPlane

def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            exit()
    
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
    pygame.init()
    
    screen = pygame.display.set_mode((480, 680), 0, 32)
    backgroud = pygame.image.load('picture/background.png')
    #myplane = pygame.image.load('picture/hero.gif')
    
    game_info = True
    
    while game_info:
        screen.blit(backgroud, (0, 0))
        #screen.blit(myplane, (190, 520))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    game_info = False
                    print(game_info)
                    break
        #key_control()
        time.sleep(0.01)
    
def game_loop():
    screen = pygame.display.set_mode((480, 680), 0, 32)
    background = pygame.image.load('picture/background.png')
    myplane = MyPlane(screen)
    game_on = True
    
    while game_on :
        screen.blit(background, (0, 0))
        
        key_control(myplane)
        myplane.display()
        
        
        pygame.display.update()
        #time.sleep(0.1)
               

def main():
    pygame.init()
    start_game_info()
    game_loop()

if __name__ =="__main__":
    main()
    
    