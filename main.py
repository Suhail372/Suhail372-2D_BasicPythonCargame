from logic import Car
import pygame
import time
import random
clock=pygame.time.Clock()
pygame.init()
gray=(119,118,110)
win=pygame.display.set_mode((500,600))
strip=pygame.image.load("strip.jpg")
run=True
win.fill(gray)
ystrip=pygame.image.load("yellow_strip.jpg")
pygame.display.set_caption('First Game')
car=pygame.image.load("car2.jpg") 
e_car=pygame.image.load("enemycar.jpg")
font=pygame.font.SysFont("arial", 40)
score_font=pygame.font.SysFont('comicsansms',20)
gameover_display1=font.render("Game Over",True,(250,200,243))
gameover_display2=font.render("Press SPACE to restart",True,(250,200,243))








c=Car(250,445,56,125)
run=True   
count=0
while run:
   
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if not c.gameover:
        if c.x>100 and c.x+c.w<400:

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                c.x-=c.v



            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                c.x+=c.v
        else:
            
            c.gameover=True

        
        if c.enemyright1==False and c.enemyleft1==False and c.enemyright2==False and c.enemyleft2==False and c.enemyright3==False and c.enemyleft3==False:
            k=random.randint(1,1000)
            if k%(16)==0:
                if c.objl1==0:
                    c.enemyleft1=True
                    c.objl1+=1
                elif c.objr1==0:
                    c.enemyright1=True
                    c.objr1+=1
                elif c.objl2==0:
                    c.enemyleft2=True
                    c.objl2+=1
                elif c.objr2==0:
                    c.enemyright2=True
                    c.objr2+=1
                elif c.objl3==0:
                    c.enemyleft3=True
                    c.objl3+=1


                elif c.objr3==0:
                    c.enemyright3=True
                    c.objr3+=1
    else:
        if keys[pygame.K_SPACE]:
            c.gameover=False
            c.x=250
            c.score=0
        count=0
    c.redraw()

pygame.quit()