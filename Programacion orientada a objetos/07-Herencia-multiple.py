class Padre:
    def hablar(self):
        print("Hola")
        
class Madre:
    def reir(self):
        print("ja ja ja")
        
    def hablar(self):
        print("que tal")    
            

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()

#Orden en que se resuelven el orden de los metodos

print(Nieto.__mro__)