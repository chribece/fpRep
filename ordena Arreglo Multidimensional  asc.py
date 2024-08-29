# Definir la matriz bidimensional de 3x3
matriz = [
    [30, 20, 10],
    [60, 50, 40],
    [90, 80, 70]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)
    # Implementación de Bubble Sort corregida
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if fila[j] > fila[j + 1]:  # Comparar elementos adyacentes
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar si están en el orden incorrecto

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Pedir al usuario que ingrese el número de fila a ordenar (0, 1, o 2)
fila_a_ordenar = int(input("\nIngresa el índice de la fila que deseas ordenar (0, 1, o 2): "))

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz después de ordenar la fila", fila_a_ordenar, ":")
imprimir_matriz(matriz)
