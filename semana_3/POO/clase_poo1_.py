import math
class Punt:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self,x1):
        self.x = x1

    def set_y(self,y1):
        self.y = y1
    
    def distancia_al_origen(self):
        return math.sqrt(self.x**2 + self.y**2)



p1 = Punt(1,1)
# print(p1.get_x())
# print(p1.get_y())

p1.set_x(4)
p1.set_y(3)
# print(p1.get_x())
# print(p1.get_y())

print(p1.distancia_al_origen())