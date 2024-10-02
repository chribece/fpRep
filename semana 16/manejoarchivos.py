# Escritura interactiva en el archivo 'my_notes.txt'
file = open('my_notes.txt', 'w')

# Pedimos al usuario que ingrese varias líneas de texto
print("Escribe tres líneas de notas. Escribe una línea y presiona Enter:")

for i in range(1, 4):
    nota = input(f"Ingrese la línea {i}: ")
    file.write(nota)
    file.write("\n")

# Cerramos el archivo después de escribir
file.close()
print("Notas guardadas en 'my_notes.txt'.")

# Abrimos el archivo 'my_notes.txt' para lectura
file = open('my_notes.txt', 'r')

# Leemos todas las líneas del archivo
lineas = file.readlines()

# Cerramos el archivo después de leer
file.close()

# Mostrar las opciones al usuario
print("\nTus notas se han guardado. Elige una opción:")
print("1. Ver todas las notas.")
print("2. Ver una línea específica.")

opcion = input("\nIntroduce 1 o 2: ")

if opcion == "1":
    # Mostrar todas las líneas
    print("\n--- Todas las Notas ---")
    for linea in lineas:
        print(linea.strip())  # Mostramos cada línea eliminando saltos de línea adicionales
elif opcion == "2":
    # Preguntar al usuario cuál línea quiere ver
    num_linea = int(input(f"\nIntroduce el número de línea (1-{len(lineas)}): "))

    if 1 <= num_linea <= len(lineas):
        print(f"\n--- Línea {num_linea}: ---")
        print(lineas[num_linea - 1].strip())
    else:
        print("Número de línea inválido.")
else:
    print("Opción no válida.")
