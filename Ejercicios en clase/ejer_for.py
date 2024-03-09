# Pedir al usuario que ingrese un rango
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número final del rango: "))

# Inicializar variables para la suma de pares e impares
suma_pares = 0
suma_impares = 0

# Calcular la suma de pares e impares en el rango dado
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

# Imprimir resultados
print(
    f"La suma de los números pares en el rango de {inicio} a {fin} es: {suma_pares}")
print(
    f"La suma de los números impares en el rango de {inicio} a {fin} es: {suma_impares}")
