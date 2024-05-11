class Pajaro:

    alas = True
 
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print('pio, mi color es {}'.format(self.color))
        
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        # 2-Los metodos de instancia pueden invocar a otros metros.
        self.piar()
    
    # 1- Metodos de instancia ya que afectana al self basicamente a cada una de las instancias.
    #Accede a los atributos de la instancia y los va a modificar.     
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}") 
    
    # 4 - Metodo de clase: No necesitan una instancia para poder ejecutarse, no pueden acceder a los atributos de instancia     
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        # 6
        #No me permite ya que poner_huevos no me resibe como argumento a self sino a cls
        #print(f"Es de color {self.color}")
        
        # 7 Se puede acceder a travez de los metodos de clase a los atributos de clase y modificarlos
        cls.alas = False
        print (Pajaro.alas)
    
    # 8 
    # Estos metodos estaticos no se refieren ni a la clase ni a la instancia
    # Estos metodos no púeden modificar el estado de una instancia
    # Ni tampoco pueden cambiar los atributos de la clase 
    @staticmethod    
    def mirar():
        print("El pajaro mira")    
             
        
        
piolin = Pajaro('amarillo', 'canario')
############################
piolin.pintar_negro()

##########################
# 3- Modificar el estado de la clase
piolin.alas = False
print(piolin.alas)


#############################
# 5- 

Pajaro.poner_huevos(3)


# 9
################################







       
            