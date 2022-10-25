from sky import Sky
from ship import Ship
import random
import pygame

class Game:
    
    def __init__(self):
        self.ship=Ship() #Crear la nave
        self.width=800 #Ancho de la pantalla
        self.height=800 #Alto de la pantalla
        self.mySky=Sky(self.width, self.height, 1600) #Crear el cielo
        self.screen=pygame.display.set_mode((self.width,self.height)) #Crear la pantalla
        self.clock=pygame.time.Clock() #Crear el reloj para controlar los fps
        self.fps=60 
        self.sprites= pygame.image.load("Matamarcianos/sprites.png") #Cargar la hoja de imágenes
        self.shipsprite=pygame.Surface((64,64)).convert() #Crear una superficie para la nave
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64)) #Cortar la nave de la hoja de imágenes

        
    def checkKeys(self):
        #Comprobar las teclas pulsadas
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.ship.direction="RIGHT" 
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        else: self.ship.direction="STOP"
        
        #Definir los limites de la pantalla
        if self.ship.x > self.width-64: self.ship.x=self.width-64 #Limite derecho
        if self.ship.x < 8: self.ship.x=8 #Limite izquierdo
        

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
            
            self.mySky.move() #Mover las estrellas
            self.ship.move() #Mover la nave
            x=self.ship.x #Posicion x de la nave
            y=self.ship.y #Posicion y de la nave
            self.screen.blit(self.shipsprite, (x,y)) #Dibujar la nave
            self.clock.tick(self.fps) #Controlar los fps
            self.checkKeys() #Comprobar las teclas
            pygame.display.flip() #Actualizar la pantalla


myGame=Game() #Creamos un objeto de la clase Game
myGame.run() #Ejecutamos el método run del objeto myGame