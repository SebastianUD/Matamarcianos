from sky import Sky
from ship import Ship
import random
import pygame

class Game:
    
    def __init__(self):
        self.ship=Ship()
        self.width=800
        self.height=800
        self.mySky=Sky(self.width, self.height, 1600)
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        self.fps=60
        #Cargar la hoja de imágenes
        self.sprites= pygame.image.load("Matamarcianos/sprites.png")
        self.shipsprite=pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64))

        
    def checkKeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.ship.direction="RIGHT"
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        else: self.ship.direction="STOP"
        #definir los limites de la pantalla
        if self.ship.x > self.width-64: self.ship.x=self.width-64
        if self.ship.x < 8: self.ship.x=8
        

    def run (self):
        pygame.init()
        
        control=True
        while control:
            self.screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen, (r,g,b), star, 1)
            
            self.mySky.move()
            self.ship.move()
            x=self.ship.x
            y=self.ship.y
            self.screen.blit(self.shipsprite, (x,y))
            self.clock.tick(self.fps)
            self.checkKeys()
            pygame.display.flip()

#Siempre hacer un objeto de la clase para que esta haga algo
myGame=Game()
myGame.run()     