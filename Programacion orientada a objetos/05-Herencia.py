# class Animal:
#     pass

# class Pajaro(Animal):
#     pass

# #Permite ver de quien hereda esta clase
# print(Pajaro.__bases__)

# #Permite verificar que Animal trasmite su herencia a pajaro
# print(Animal.__subclasses__)

class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, 'amarillo')


piolin.nacer()

