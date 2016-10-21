import pygame
import random


class Rock(pygame.sprite.Sprite):


    def __init__(self):
        super(Rock,self).__init__()
        self.image = pygame.image.load("asteroid")
        self.rect = self.image.get_rect()

    def update():
        self.rect.x = 5
        if self.rect.y >display_height:
            self.rect.x = 600 - display_width
            self.rect.y = random.randrange(0, display_height)

pygame.init()
display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))

rock_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

def make_enemy():
    enemy1 = Rock()

    for i in range(1):      
        enemy1.rect.x = random.randrange(display_width)
        enemy1.rect.y = random.randrange(display_height)
        enemy1.rect.x = x
        enemy1.rect.y = y
   

        rock_list.add(enemy1)
        all_sprites_list.add(enemy1)
        screen.blit(enemy1,(x,y))

make_enemy()
   
    









