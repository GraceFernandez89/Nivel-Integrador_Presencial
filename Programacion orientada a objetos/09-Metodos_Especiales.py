# mi_lista = [1,1,1,1,1,1,1]
# #Quiero saber cuando elemento tiene mi lista
# print(len(mi_lista))

# class Objeto:
#     pass


# mi_objeto = Objeto()
# print(mi_objeto)


class CD:
    
    def __init__(self, autor, titulo, canciones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    #Lo que hace este metodo especial es ayudarme a mi como creador de clases
    #a definir la forma en que yo quiero que se manifieste un string de mi clase
    #cada vez que un metodo lo solicite     
    def __str__(self):
         return f"Album : {self.titulo} de {self.autor}"
    
    #Para establecer que sucesa cuando alguien pida el largo de mis cds 
    def __len__(self):
        return self.canciones
            
        
        
mi_cd = CD('Pink Floyd', 'The Wall', 24)
print(str(mi_cd))
print(mi_cd) 
print(len(mi_cd))        