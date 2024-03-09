# Vamos a crear un programa que solicita al usuario que adivine un número aleatorio entre 1 y 10.
# El programa continuará pidiendo al usuario que adivine hasta que lo haga correctamente:
import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Solicitar al usuario que adivine el número
adivinanza = None  # Variable vacia o sin un valor definido
intentos = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1

print(f"¡Correcto! El número secreto era {numero_secreto}.")
print(f"¡Lo lograste en {intentos} intentos!")
