ventas = [12000, 8500, 15000, 9200, 18000]
total = 0
contador = 0
while contador < 6:
    if total >= 1:
        print(contador,":","$", total)
    contador += 1
    for venta in ventas:
        total += venta

print("TOTAL =",total)

