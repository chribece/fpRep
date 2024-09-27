#creamos el diccionario
informacion_personal={"nombre":"Christian Becerra","edad":40,"ciudad":"Quito","profesion":"Estudiante"

}

print("Paso 1: Diccionario inicial creado:")
print(informacion_personal)
print("\n")

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"]="MANTA"
print("Paso 2: El valor de 'ciudad' ha sido modificado a 'Manta':")
print(informacion_personal)
print("\n")


#Agrega una nueva clave-valor al diccionario
informacion_personal["Estado civil"]="Divorciado"
print("Paso 3: Se agrega clave de 'Estado civil' y su valor 'Divorciado':")
print(informacion_personal)
print("\n")


#Verifica si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0997474028"
    print("Paso 4: La clave 'telefono' no existía, se ha agregado con el valor '0997474028':")
else:
    print("Paso 4: La clave 'telefono' ya existía en el diccionario.")

print(informacion_personal)
print("\n")


#Elimina la clave "edad" del diccionario
del informacion_personal["edad"]
print("Paso 5: La clave 'edad' ha sido eliminada del diccionario:")
print(informacion_personal)
print("\n")


#Imprime el diccionario resultante
print("Diccionario final después de todas las modificaciones:")
print(informacion_personal)