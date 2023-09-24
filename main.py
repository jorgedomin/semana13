def calcular_descuento(monto_total):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamadas a la función calcular_descuento
monto_compra1 = 1000
porcentaje_descuento = 10
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 200
porcentaje_descuento2 = 50
descuento2 = calcular_descuento(monto_compra2)
monto_final2 = monto_compra2 - descuento2

# Salida de resultados
print(f"Compra 1: Monto Total = ${monto_compra1}, Descuento = ${descuento1}, Monto Final = ${monto_final1}")
print(f"Compra 2: Monto Total = ${monto_compra2}, Descuento = ${descuento2}, Monto Final = ${monto_final2}")
