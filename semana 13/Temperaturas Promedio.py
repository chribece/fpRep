
# lista nombres de  ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Datos de temperaturas para 3 ciudades durante 4 semanas
# Matriz 3D: ciudades x semanas x días
temperaturas = [
    [[18, 20, 22, 21, 19, 23, 20],  # Semana 1 de Quito
     [20, 21, 22, 24, 19, 18, 22],  # Semana 2 de Quito
     [19, 21, 23, 20, 22, 25, 24],  # Semana 3 de Quito
     [21, 22, 23, 21, 19, 20, 22]],  # Semana 4 de Quito

    [[28, 29, 30, 31, 32, 33, 30],  # Semana 1 de Guayaquil
     [30, 31, 29, 28, 32, 30, 31],  # Semana 2 de Guayaquil
     [29, 30, 31, 32, 31, 33, 32],  # Semana 3 de Guayaquil
     [31, 32, 30, 29, 33, 32, 31]],  # Semana 4 de Guayaquil

    [[14, 15, 16, 17, 18, 16, 17],  # Semana 1 de Cuenca
     [16, 17, 18, 15, 14, 16, 17],  # Semana 2 de Cuenca
     [18, 19, 17, 16, 14, 15, 18],  # Semana 3 de Cuenca
     [17, 18, 19, 15, 14, 16, 17]]  # Semana 4 de Cuenca
]


# Función para calcular el promedio de temperatura para cada ciudad
def calcular_promedio_por_ciudad(temperaturas, ciudades):
    num_ciudades = len(ciudades)
    num_semanas = len(temperaturas[0])
    num_dias = len(temperaturas[0][0])

    promedios_ciudades = {}

    # Calcular el promedio de temperatura de todas las semanas y días
    for i in range(num_ciudades):
        suma_total = 0
        total_dias = num_semanas * num_dias

        for semana in range(num_semanas):
            for dia in range(num_dias):
                suma_total += temperaturas[i][semana][dia]

        promedio = suma_total / total_dias
        promedios_ciudades[ciudades[i]] = promedio

    return promedios_ciudades


# Función para mostrar el promedio de temperatura de una ciudad específica
def mostrar_promedio_ciudad_especifica(ciudades, temperaturas, ciudad):
    if ciudad in ciudades:
        indice_ciudad = ciudades.index(ciudad)
        suma_total = 0
        total_dias = len(temperaturas[0]) * len(temperaturas[0][0])  # Semanas x Días
        for semana in range(len(temperaturas[0])):
            for dia in range(len(temperaturas[0][0])):
                suma_total += temperaturas[indice_ciudad][semana][dia]
        promedio = suma_total / total_dias
        print(f"\nPromedio de temperatura de {ciudad}: {promedio:.2f}°C")
    else:
        print(f"La ciudad {ciudad} no está en la lista.")


# Menú interactivo
def menu_interactivo():
    while True:
        print("\nOpciones:")
        print("1. Mostrar promedio de temperatura de todas las ciudades")
        print("2. Mostrar promedio de temperatura de una ciudad específica")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Mostrar promedio de todas las ciudades
            promedios = calcular_promedio_por_ciudad(temperaturas, ciudades)
            print("\nPromedios de temperatura por ciudad durante 4 semanas:")
            for ciudad, promedio in promedios.items():
                print(f"{ciudad}: {promedio:.2f}°C")
        elif opcion == "2":
            # Solicitar ciudad específica y mostrar su promedio
            ciudad = input("Ingresa el nombre de la ciudad (Quito, Guayaquil, Cuenca): ")
            mostrar_promedio_ciudad_especifica(ciudades, temperaturas, ciudad)
        elif opcion == "3":
            print("¡Gracias por usar el sistema! ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


# Programa principal
def main():
    print("¡Bienvenido al sistema de temperaturas de ciudades!")
    menu_interactivo()


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
