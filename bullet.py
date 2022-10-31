class Bullet:
    def __init__(self):
        self.bullets = [] #Lista de balas
        self.condition = "STOP" #Condición de la bala

    def shoot (self,x,y):
        if self.condition == "DISPARADO":
            for i in range(1): #Crear una bala
                self.bullets.append([x,y]) #Añadir la bala a la lista
                self.condition = "STOP" 
            
        for bullet in self.bullets: #Mover la bala
            bullet[1]-=10
            if bullet[1] <= -20: 
                self.bullets.remove(bullet) #Eliminar la bala si sale de la pantalla           
        


        

        
 