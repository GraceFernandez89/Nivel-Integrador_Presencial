
lista = [1, 2.5, 'DevCode', [5, 6], 4]

print(lista[0])  # 1
print(lista[1])  # 2.5
print(lista[2])  # DevCode
print(lista[3])  # [5,6]
print(lista[3][0])  # 5
print(lista[3][1])  # 6
print('Hicimos este cambio ->', lista[1:4])  # [2.5, 'DevCode']
print(lista[1:6])  # [2.5, 'DevCode', [5, 6], 4]


nombres = ["Ana", "Bernardo"]
edades = [22, 21]
lista = [nombres, edades]
print(lista)
nombres += ["Cristina"]
print(lista)


# En el caso de querer añadir un elemento a una lista en Python podemos hacerlo de dos formas. La primera será utilizando el método .append().

lista.append(6)
print(lista)

#x = range(10)
# print(x)


# lista=[[1,2,3],[4,5,6],[7,8,9]]
# print(lista)
# print(lista[1][2])

# Acceder a todos los elementos de la primera componente
# lista=[[1,2,3],[4,5,6],[7,8,9]]
# for x in range(len(lista[0])):
#   print(lista[2][x])

# Imprime cada elemento entero de la lista contenida en la lista principal
# for k in range(len(lista)):
#   for x in range(len(lista[k])):
#     print(lista[k][x])

# lista=[1,2,3,4,5,6]
# print(lista[1:5:1])

# lista=['A','B','C']

# for i in lista:
#   print(i, end='')


# lista=[[1,3,5,7,9],[2,4,6,8,10]]

# for k in range(len(lista)):
#     suma=0
#     for x in range(len(lista[k])):
#        suma = suma + lista[k][x]
#     print(suma)
