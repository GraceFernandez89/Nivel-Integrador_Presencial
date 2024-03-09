# Primer ejercicio
# Pedir al usuario que ingrese un año
# Este programa primero lee un año ingresado por el usuario.
# Luego, verifica si el año es bisiesto según las reglas mencionadas anteriormente y muestra el resultado correspondiente.
year = int(input("Ingrese un año: "))

# Verificar si es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")

# 2024 es año bisiesto
