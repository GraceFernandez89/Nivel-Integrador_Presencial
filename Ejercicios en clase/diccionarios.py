# # Diccionario
# diccionario = {'Eduardo': 1, 'Fernando': 2, 'Uriel': 3, 'Rafael': 4}
# print(diccionario)
# print(diccionario.values())
# print(diccionario.keys())


# diccionario2 = {
#     "clave1": 234,
#     "cadena": True,
#     "clave3": "Valor 1",
# }
# print(diccionario2)
# print(type(diccionario))
# print(diccionario2['clave1'])


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones_adicional = dict(django=2.1)
# print(versiones_adicional)
# versiones.update(versiones_adicional)
# print(versiones)


# Diccionario--------------------
diccionario3 = {
    'azul': 'blue',
    'amarillo': 'yellow',
    'rojo': 'red',
    'verde': 'green'
}

# Agregar elementos al diccionario---------------------------

diccionario3['cafe'] = 'brown'
print(diccionario3)

print(diccionario3)

# # Modificar elementos-------------------------

# diccionario3['cafe'] = 'cafe'

# print(diccionario3)


# # Eliminar un elemento----------------------------
# # Utilizamos la funcion del()-----------------------

# del(diccionario3['azul'])
# print(diccionario3)


# # white = input("Ingrese la palabra blanco en ingles:")

# # diccionario3['blanco'] = white

# # print(diccionario3)

# diccionario['cafe'] = 'brown'
# print(diccionario3)


# # Tuplas

# diccionario_persona = {
#     'Felipe': [80, 1.80],
#     'Maria': [60, 1.60],
#     'Fernando': [90, 1.90]
# }

# print(diccionario_persona)
# print(diccionario_persona['Maria'][0])

# # Para que nuestro diccionario quede limpio se utiliza el metodo clear()

# estudiantes = {
#     1: 'William Guerrero',
#     2: 'Sara Sofia Cuayal',
#     3: 'Felipe Agrega'
# }

# estudiantes.clear()
# print(estudiantes)
# print(estudiantes)

# # Cuantos estudiantes hay en mi diccionario(cuantos elementos hay en
# # el diccionario)

# estudiantes = {
#     1: 'William Guerrero',
#     2: 'Sara Sofia Cuayal',
#     3: 'Felipe Agrega'
# }

# print(len(estudiantes))

# # #Busqueda directa en un diccionario

# estudiantes = {
#     1: 'William Guerrero',
#     2: 'Sara Sofia Cuayal',
#     3: 'Felipe Agrega'

# }
# print(1 in estudiantes)
# print('William Guerrero' in estudiantes[1])
