# Definir la matriz bidimensional de 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definir la función de búsqueda
def buscar_valor(matriz, valor):
    # Recorrer cada fila y columna de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna) si se encuentra el valor
    return None  # Retorna None si el valor no se encuentra

# Mostrar la matriz al inicio
print("La matriz es:")
imprimir_matriz(matriz)

# Pedir al usuario que ingrese el valor a buscar
valor_a_buscar = int(input("\nIngresa el número que deseas buscar en la matriz: "))

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"Valor {valor_a_buscar} se encuentra en la posición: {posicion}")
else:
    print(f"Valor {valor_a_buscar} no se encontró en la matriz.")