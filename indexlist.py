


vocales=["a", "e", "i", "o", "u","a"]

print(f"Lista: {vocales}")
print(f"La letra a esta en la posición: {vocales.index('a')}")
print(f"La letra i esta en la posición: {vocales.index('i')}")
print(f"La letra u en el rango 2-final esta en la posición: {vocales.index('u',2)}")
print(f"La letra i en el rango 2-4 esta en la posición: {vocales.index('i',2, 4)}")



vocales2=["o", "e", "a", "u", "i"]
print(f"Vocales Desordenadas: {vocales2}")
vocales2.sort(reverse=True)
print(f"U-A: {vocales2}")
print(f"A-U:", sorted(vocales2))