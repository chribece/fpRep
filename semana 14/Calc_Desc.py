
#funcion para calcular descuento

def calcular_descuento(monto,descuento=10):
    descuento=monto*(descuento/100)
    return descuento

#llamada 1 funcion calcular descuento

monto1=1000
descuento1=calcular_descuento(monto1)
montof=monto1-descuento1
print(f"Monto total: ${monto1}")
print(f"Descuento 10%: ${descuento1}")
print(f"Valor a cancelar: ${montof}\n")

#llamada 2 funcion calcular descuento
monto2=100
descuento2=calcular_descuento(monto2)
montof2=monto2-descuento2
print(f"Monto total: ${monto2}")
print(f"Descuento 10%: ${descuento2}")
print(f"Valor a cancelar: ${montof2}\n")

#llamada 3 funcion calcular descuento con argumento porcentaje de descuento diferente
monto3=1500
porcentaje3=15
descuento3=calcular_descuento(monto3,porcentaje3)
montof3=monto3-descuento3
print(f"Monto total: ${monto3}")
print(f"Descuento {porcentaje3}%: ${descuento3}")
print(f"Valor a cancelar: ${montof3}")

