import pygame
import random
import math
import os


WIDTH = 800
HEIGHT = 600
FPS = 75

#Colors
BLACK = (0,0,0)
RED = (255,0,0)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

#background

background = pygame.image.load(os.path.join(img_folder,"bg1.jpg"))

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"side.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HEIGHT / 2)
        self.y_speed = 1
        
    def update(self):
        self.rect.x += 1
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -1
        if self.rect.top < 200:
            self.y_speed = 1
        if self.rect.left > WIDTH:
            self.rect.right = 0

#Initiale pygame
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True

while running:
    
    clock.tick()
    
    window.fill(BLACK)
    window.blit(background,(0,0))
    
    #events and inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update objects
    all_sprites.update()
    
    #draw / render
    all_sprites.draw(window)
    
    pygame.display.flip()
    
pygame.quit()
