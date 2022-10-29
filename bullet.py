from ship import Ship
class Bullet:
    def __init__(self):
        self.ship=Ship()
        self.bullets = []
        self.condition = "STOP"
    
    
    def shoot (self,x,y):
        if self.condition == "DISPARADO":
            for i in range(1): #Crear una bala
                self.bullets.append([x,y])
                self.condition = "STOP"
            
        for bullet in self.bullets: #Mover la bala
            bullet[1]-=10
            if bullet[1] < 0:
                self.bullets.remove(bullet)
        


        

        
 