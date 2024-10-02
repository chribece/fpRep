
#creamos archivo my_notes.txt
#Tres líneas en el archivo

"""file=open('my_notes.txt', 'w')
file.write("test archivo")
file.write("\n")
file.write("Primera linea archivo")
file.write("\n")
file.write("Segunda linea archivo")
file.write("\n")
file.write("Tercera linea archivo")
file.write("\n")

file.close()#cerrar documento"""

#Abrir archivo my_notes.txt.
file=open('my_notes.txt', 'r')

#print(file.read())
lineas=file.readlines()
print(lineas)
file.close()#cerrar documento
