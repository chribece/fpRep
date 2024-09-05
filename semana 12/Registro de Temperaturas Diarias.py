# Importar la biblioteca random para generar temperaturas aleatorias
import random

# Definir nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Definir dimensiones de la matriz
num_ciudades = len(ciudades)  # Número de ciudades
num_dias = 7      # Número de días (Lunes, Martes, Miércoles, etc.)
num_semanas = 4   # Número de semanas

# Crear la matriz 3D
temperaturas = [[[random.randint(15, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Calcular y mostrar el promedio de temperaturas para cada ciudad por cada semana
for i in range(num_ciudades):
    print(f"Ciudad: {ciudades[i]}")
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio_semanal = suma_temperaturas / num_dias
        print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio_semanal:.2f}°C")
    print()  # Línea en blanco entre ciudades
