
t = ('esto es una cadena', 'b', 'c', 'd', 'e')
print(t)
print(t[0])

t1 = ('a',)  # Tupla
print(type(t1))

t2 = ('a')  # String
print(type(t2))


# Otro ejemplo
txt = "but soft what light in yonder window breaks"
palabras = txt.split()
print(palabras)

l = list()
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)

l.sort(reverse=True)
print(l)

res = list()

for longitud, palabra in l:
    res.append(palabra)
print(res)


m = ['have', 'fun']
x, y = m
print(x)
print(y)


# m = [ 'have', 'fun' ]
# (x, y) = m
# print(x)
# print(y)


# Mi primer CRUD

# tareas={
#     '01':{
#         'descripcion':'ir a mercar',
#         'estado':'pendiente',
#         'tiempo':60
#     },
#     '02':{
#         'descripcion':'Estudiar',
#         'estado':'pendiente',
#         'tiempo':180
#     },
#     '03':{
#         'descripcion':'Hacer ejercicio',
#         'estado':'pendiente',
#         'tiempo':50
#     }

# }


# print("Adiconar tareas")
# print("Consultar tareas")
# print("Actualizar tarea")
# print("Eliminar tarea")
# print("Salir")
# opcion=int(input("Ingrese una opcion:"))


# if opcion==1:
#     print()
#     print("--->Adicionando tarea")
#     identificador=str(input("Ingrese el identificador de la tarea: "))
#     descripcion=str(input("Ingrese descripcion de la tarea: "))
#     estado=str(input("Ingrese el estado inicial de la tarea: "))
#     tiempo=int(input("Ingrese el tiempo de realizacion: "))

#     tareaNueva={
#         'descripcion':descripcion,
#         'estado':estado,
#         'tiempo':tiempo
#     }

#     #tareas=create(tareas,identificador,tareaNueva)
#     def create(tareas,identificador,tareaNueva):
#         tareas[identificador]=tareaNueva
#         #tareas=create(tareas,identificador,tareaNueva)
#         return(tareas)
#     print(create(tareas,identificador,tareaNueva))
# elif opcion==2:
#     print()
#     print("-> Listar Tareas")
#     print()
#     def read(tareas):
#         for identificador, tarea in tareas.items():
#             print(identificador,'- ',end='')
#             for nombre_atriuto, atributo in tarea.items():
#                 print(atributo, ', ', end='')
#                 print()

#     print(read(tareas))
