from sky import Sky
from ship import Ship
from bullet import Bullet
import pygame, random

class Game:
    
    def __init__(self):
        self.ship=Ship() #Crear la nave
        self.bullet=Bullet() #Crear la bala
        self.width=800 #Ancho de la pantalla
        self.height=800 #Alto de la pantalla
        self.mySky=Sky(self.width, self.height, 1600) #Crear el cielo
        self.screen=pygame.display.set_mode((self.width,self.height)) #Crear la pantalla
        self.clock=pygame.time.Clock() #Crear el reloj para controlar los fps
        self.fps=60
        self.sprites=pygame.image.load("Matamarcianos/sprites.png") #Cargar la hoja de imágenes
        self.shipsprite=pygame.Surface((64,64)).convert() #Crear una superficie para la nave
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64)) #Cortar la nave de la hoja de imágenes
        self.shipsprite.set_colorkey((0,0,0)) #Quitar el fondo de la nave
        self.bulletsprite=pygame.image.load("Matamarcianos/bullet.png").convert() #Dibujar la balla
        self.bulletsprite.set_colorkey((0,0,0)) #Quitar el fondo de la bala
        
        
    def checkKeys(self):
        #Comprobar las teclas pulsadas
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.ship.direction="RIGHT" 
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        else:
            self.ship.direction="STOP" 
            

    def run (self):
        pygame.init()
        
        control=True
        while control:
            self.screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Cerrar si se pulsa la X de la ventana
                    pygame.quit()
                if event.type==pygame.KEYDOWN: #Comprobar si se pulsa una tecla
                    if event.key==pygame.K_SPACE: #Comprobar si se pulsa la tecla espacio
                        self.bullet.condition="DISPARADO"

            #Dibujar las estrellas
            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen, (r,g,b), star, 1)
            
            #Dibujar las balas
            for bullet in self.bullet.bullets:
                self.screen.blit(self.bulletsprite,(bullet[0],bullet[1]))
                
            #Definir los limites de la pantalla
            if self.ship.x > self.width-64: self.ship.x=self.width-64 #Limite derecho
            if self.ship.x < 8: self.ship.x=8 #Limite izquierdo
            
            self.mySky.move() #Mover las estrellas
            self.ship.move() #Mover la nave
            x=self.ship.x #Posicion x de la nave
            y=self.ship.y #Posicion y de la nave
            self.screen.blit(self.shipsprite, (x,y)) #Dibujar la nave
            self.clock.tick(self.fps) #Controlar los fps
            self.checkKeys() #Comprobar las teclas
            self.bullet.shoot(self.ship.x+5,self.ship.y-15) #Disparar
            pygame.display.flip() #Actualizar la pantalla


myGame=Game() #Creamos un objeto de la clase Game
myGame.run() #Ejecutamos el método run del objeto myGame