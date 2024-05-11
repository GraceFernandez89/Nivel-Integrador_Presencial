class Pajaro:
    #Atributo de clase
    alas = True
#Se define el metodo constructor en donde vamos a asiganrle atributos al pajaro
#Se define self como el mismo y luego el atributo de instancia que vamos a nececitar     
    def __init__(self, color, especie):
        #Self seria la instancia del objeto que se va a crear
        self.color = color
        self.especie = especie
        
mi_pajaro = Pajaro('negro','Tucan')   
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(f"Mi pajaro es de color {mi_pajaro.color} de especie {mi_pajaro.especie}") 


print(Pajaro.alas)
print(mi_pajaro.alas)     
        