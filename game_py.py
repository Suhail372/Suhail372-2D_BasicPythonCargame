import pygame
import time
import random

clock=pygame.time.Clock()
pygame.init()
gray=(119,118,110)
win=pygame.display.set_mode((500,6600))

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


class Car:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.v=3
        self.score=0
        self.move=0
        self.pos=[-120,0,120,240,360,480]
        self.objl1=0
        self.objr1=0
        self.objl2=0
        self.objr2=0
        self.objl3=0
        self.objr3=0
        self.objm1=0
        self.objm2=0
        self.objm3=0
        self.enemymiddle1=False
        self.enemymiddle2=False
        self.enemymiddle3=False
        self.enemyleft1=False
        self.enemyright1=False
        self.enemyleft2=False
        self.enemyright2=False
        self.enemyleft3=False
        self.enemyright3=False
        self.gameover=False
        self.car_rect=car.get_rect()
        self.enemy_pos=[]   
    #MAIN DISPLAY
    def redraw(self):
        if not self.gameover:
            self.draw_road()
            
            self.draw_enemies()
            self.score+=1
            win.blit(car,(self.x,self.y))
            
            self.car_rect=car.get_rect()
            self.car_rect.bottom=self.y+self.h
            self.car_rect.centerx=self.x+25

            
        else:
            self.Game_over()
        
            
        pygame.display.update()

    def draw_enemies(self):
        if self.objl1<=725 and self.objl1>0:
                self.objl1=self.e_left(self.objl1,130)
        else:
            self.objl1=0
        if  self.objl1>=250:
            self.enemyleft1=False

        if self.objl2<=725 and self.objl2>0:
            self.objl2=self.e_left(self.objl2,110)
        else:
            self.objl2=0
        if self.objl2>=250:
            self.enemyleft2=False

        if self.objl3<=725 and self.objl3>0:
            self.objl3=self.e_left(self.objl3,120)
        else:
            self.objl3=0
        if self.objl3>=250:
            self.enemyleft3=False
        #CHECING FOR RIGHT
        if self.objr1<=725 and self.objr1>0:
            self.objr1=self.e_left(self.objr1,400)
        else:
            self.objr1=0
        if self.objr1>=250:
            self.enemyright1=False
        if self.objr2<=725 and self.objr2>0:
            self.objr2=self.e_left(self.objr2,390)
        else:
            self.objr2=0
        if self.objr2>=250:
            self.enemyright2=False

        if self.objr3<=725 and self.objr3>0:
            self.objr3=self.e_left(self.objr3,380)
        else:
            self.objr3=0
        if self.objr3>=250:
            self.enemyright3=False
        #CHECKING FOR MIDDLE
       
        
        

    #DRAWING ENVIRONMENT 
    def draw_road(self):
        win.fill(gray)
        p=self.pos
        score_heading=score_font.render("Score:",True,(0,0,0))
        score_display=score_font.render(str(self.score//10),True,(0,0,0))
        win.blit(score_heading,(410,10))
        win.blit(score_display,(410,60))
        win.blit(ystrip,(298,p[0]+self.move%120))
        win.blit(ystrip,(298,p[1]+self.move%120))
        win.blit(ystrip,(298,p[2]+self.move%120))
        win.blit(ystrip,(298,p[3]+self.move%120))
        win.blit(ystrip,(298,p[4]+self.move%120))
        win.blit(ystrip,(298,p[5]+self.move%120))
        win.blit(strip,(100,0))
        win.blit(strip,(500,0))   
        if self.move==120:
                temp=p.pop()
                p.insert(0,temp)
                self.move=0
        else:
            if self.score<3000:
                self.move+=7+1*(self.score*(0.001))
            else:
                self.move+=10
    #GAMEO OVER AND RESTART 
    def Game_over(self):
        win.fill((0,0,0))
        win.blit(gameover_display1,(175,200))
        win.blit(gameover_display2,(120,250))
        final_score=font.render(f"Your score:{str(self.score//10)}",True,(250,200,243))
        win.blit(final_score,(175,300))
        self.x=256
        self.y=445
        self.w=56
        self.h=125
        self.v=3
        self.move=0
        self.pos=[-120,0,120,240,360,480]
        self.objl1=0
        self.objr1=0
        self.objl2=0
        self.objr2=0
        self.objl3=0
        self.objr3=0
        self.enemyleft1=False
        self.enemyright1=False
        self.enemyleft2=False
        self.enemyright2=False
        self.enemyleft3=False
        self.enemyright3=False
        self.enemymiddle1=False
        self.enemymiddle2=False
        self.enemymiddle3=False

    #ENMY MOVEMENTS AND COLLISIONS:::::::
    def e_left(self,objl,x):
        win.blit(e_car,(x,-125+objl))
        e_car_rect1=e_car.get_rect()

        e_car_rect1.bottom=-125+objl+self.h-10
        e_car_rect1.centerx=x+23
        if e_car_rect1.colliderect(self.car_rect):
            self.gameover=True
        objl+=3+1*(self.score*(0.001))
        return objl
    


        
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

