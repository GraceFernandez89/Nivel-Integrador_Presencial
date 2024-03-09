# Conjunto

conjunto = set()
conjunto = {1, 2, 3, "hola"}

print(conjunto)

# no se puede guadar valores duplicados, en los conjuntos solo pueden existir valores unicos

conjunto2 = set()
conjunto2 = {1, 2, 3, "hola", 1, 2, 3}
print(conjunto2)

# Agregar mas elementos
# Son colecciones de datos desordenados asi que este valor lo pondra donde el conjunto quiera
conjunto3 = {1, 2, 3, "hola"}
conjunto3.add(9)
print(conjunto3)

# Eliminar un elemento de nuestro conjunto
conjunto4 = {1, 2, 3, "hola"}
conjunto4.discard(1)
print(conjunto4)

# Vaciar todo el conjunto
conjunto5 = {1, 2, 3, "hola"}
conjunto5.clear()
print(conjunto5)

# Buscar un elemento
conjunto6 = {1, 2, 3, "hola"}
print(8 not in conjunto6)
