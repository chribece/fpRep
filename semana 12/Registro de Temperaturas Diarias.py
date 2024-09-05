# Importar la biblioteca random para generar temperaturas aleatorias
import random

# Definir nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Definir dimensiones de la matriz
num_ciudades = len(ciudades)  # Número de ciudades
num_dias = 7      # Número de días (Lunes, Martes, Miércoles, etc.)
num_semanas = 4   # Número de semanas

# Función para crear la matriz 3D con temperaturas aleatorias
def generar_temperaturas_aleatorias():

# Crear la matriz 3D
    temperaturas = [[[random.randint(15, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in
                range(num_ciudades)]
    return temperaturas

# Función para calcular y mostrar el promedio de temperaturas para cada ciudad por cada semana
def mostrar_promedios(ciudades, temperaturas):

    # Calcular y mostrar el promedio de temperaturas para cada ciudad por cada semana
    for i in range(num_ciudades):
        print(f"\nCiudad: {ciudades[i]}")
        for semana in range(num_semanas):
            suma_temperaturas = 0
            for dia in range(num_dias):
                suma_temperaturas += temperaturas[i][semana][dia]
            promedio_semanal = suma_temperaturas / num_dias
            print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio_semanal:.2f}°C")
        print()  # Línea en blanco entre ciudades

def main():
    print("¡Bienvenido al sistema de temperaturas de ciudades!")

    # Generar temperaturas aleatorias
    temperaturas = generar_temperaturas_aleatorias()

    # Menú interactivo para mostrar los promedios de temperatura
    while True:
        print("\nOpciones:")
        print("1. Mostrar promedio de temperaturas para Quito, Guayaquil y Cuenca (automáticamente generadas)")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_promedios(ciudades, temperaturas)
        elif opcion == "2":
            print("¡Gracias por usar el sistema! ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()