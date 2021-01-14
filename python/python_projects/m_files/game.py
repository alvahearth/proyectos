import pygame as pg
from pygame import mixer
import random
import math

pg.init()

#main window (width,height)
window = pg.display.set_mode((700,700))

#background

background = pg.image.load("space_bg.png")

#background music

mixer.music.load("music.mp3")
mixer.music.play(-1)

#caption
pg.display.set_caption("Space Invaders")
icon = pg.image.load("space1.png")
pg.display.set_icon(icon)


#player
playerimg = pg.image.load("space2.png")
playerx = 300
playery = 650
player_movement_x = 0

#enemies
enemyimg = []
enemyx = []
enemyy = []
enemy_movement_x = []
enemy_movement_y = []
number_of_enemies = 10
separation = 20

for i in range(number_of_enemies):
    enemyimg.append(pg.image.load("enemy1.png"))
    enemyx.append(random.randint(32,450))
    enemyy.append(30)
    enemy_movement_x.append(2)
    enemy_movement_y.append(30)

# score
score_value = 0
font = pg.font.Font("freesansbold.ttf",25)

textx = 5
texty = 5

#game over
over_text = pg.font.Font("freesansbold.ttf",65)

#win_screen
win = pg.font.Font("freesansbold.ttf",65)

#start again screen
start_over = pg.font.Font("freesansbold.ttf",20)


#bullet
bulletimg = pg.image.load("bala (1).png")
bulletx = 0
bullety = 650    
bullet_movement_x = 0
bullet_movement_y = 3.5
bullet_state = "ready"

def show_score(x,y):
    score = font.render("Score :"+ str(score_value),True,(255,255,255))
    window.blit(score,(x,y))
    
def gameover():
    over_screen = over_text.render("GAME OVER",True,(255,255,255))
    window.blit(over_screen,(70,200))
    
def game_win():
    win_screen = win.render("GANASTE",True,(255,255,255))
    window.blit(win_screen,(70,200))
    
def restart():
    start_again = start_over.render("presiona L para volver a intentar",True,(255,255,255))
    window.blit(start_again,(125,300))
    
    

def enemy(x,y,i):
    window.blit(enemyimg[i],(x,y))

def player(x,y):
    window.blit(playerimg,(x,y))
    
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletimg,(x + 10,y + 10))
    
def iscollision(e_x,b_x,e_y,b_y):
    distance = math.sqrt((math.pow(e_x - b_x,2)) + (math.pow(e_y - b_y,2)))
    if distance < 20:
        return True
    else:
        return False
    

running = True

# Game loop
while running:
    
    window.fill((0,0,0))
    
    window.blit(background,(0,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_movement_x = -1.5 
            if event.key == pg.K_RIGHT:
                player_movement_x = 1.5 
            if event.key == pg.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerx
                    bullet(playerx,bullety)
            if event.key == pg.K_l:
                playerx = 300
                playery = 650
                #player(playerx,playery)
                #enemy(enemyx[i],enemyy[i],i)
                for i in range(number_of_enemies):
                    enemyx[i] = random.randint(32,450)
                    enemyy[i] = 30
                    #enemy(enemyx[i],enemyy[i],i)
                score_value = 0
        
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player_movement_x = 0
                
                
    playerx += player_movement_x
    
    if playerx <= 2:
        playerx = 2
    elif playerx >= 666:
        playerx = 666

    
    for i in range(number_of_enemies):
        
        if enemyy[i] >= 650:
            for j in range(number_of_enemies):
                enemyy[j] = 2000
                playery = 2000
            bullety = 650
            bullet_state = "ready"
            gameover()
            restart()
            break
        
        
        enemyx[i] += enemy_movement_x[i]
        if enemyx[i] <= 32:
            enemy_movement_x[i] = 2
            enemyy[i] += enemy_movement_y[i]
            #if enemyy[i] >= 400:
            #   enemy_movement_y[i] = 0
        elif enemyx[i] >= 450:
            enemy_movement_x[i] = -2
            enemyy[i] += enemy_movement_y[i]
            #if enemyy[i] >= 400:
            ##  enemyy[i] += enemy_movement_y[i]
                
        collision = iscollision(enemyx[i],bulletx,enemyy[i],bullety)
        if collision:
            score_value += 1
            bullety = 650
            bullet_state = "ready"
            enemyx[i] = random.randint(32,450)
            enemyy[i] = 20
        if score_value == 10:
            for j in range(number_of_enemies):
                enemyy[j] = 2000
                playery = 2000
            bullety = 2000
            bullet_state = "fire"
            game_win()
            break
            
        enemy(enemyx[i],enemyy[i],i)
            
            
    if bullety < 0 :
        bullety = 650
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet(bulletx,bullety)
        bullety -= bullet_movement_y
        
    
        
    player(playerx,playery)
    show_score(textx,texty)
            
    pg.display.update()