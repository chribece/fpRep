print(" FUNDAMENTOS DE PROGRAMACION")
print(" PARALELO:E")
print(" DESARROLLADO POR:CHRISTIAN BECERRA")

# bucle while para imprimir los primeros 5 números naturales.

print(" BUCLE WHILE NUMEROS NATURALES")
print(" ═════════════════════════════════════════════════════════")

x = 1

while x <= 5:
    print(x)
    x = x + 1

# bucle Bucle do-while Juego de adivinanza.
print(" BUCLE WHILE JUEGO ADIVINANZA")
print(" ═════════════════════════════════════════════════════════")
import random


def jugar_adivinanza():
    numero_secreto = 7  # número secreto
    adivinanza = None

    print("¡Bienvenido al juego de adivinanza!")

    while adivinanza != numero_secreto:
        adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))

        if adivinanza < numero_secreto:
            print("Demasiado bajo. Inténtalo de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Inténtalo de nuevo.")
        else:
            print("¡Felicidades! ¡Adivinaste el número secreto!")


def main():
    jugar_otra_vez = "s"

    while jugar_otra_vez.lower() == "s":
        jugar_adivinanza()
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ")

    print("¡Gracias por jugar! ¡Hasta la próxima!")


if __name__ == "__main__":
    main()

# Bucle for suma de los primeros 10 números enteros
print(" BUCLE FOR SUMA NUMEROS ENTEROS")
print(" ═════════════════════════════════════════════════════════")

# Inicializa la variable para almacenar la suma
suma = 0

for numero in range(1, 11):  # El rango es de 1 a 10 (incluido)
    suma += numero  # Suma el número actual a la variable 'suma'

    # Muestra el resultado
    print(suma)
