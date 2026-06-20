# ============================================================ Metodo con 2 condiciones ================================================= 
#ventas = [12000, 8500, 15000, 9200, 18000, 11000]
#total = 0
#for venta in ventas:
 #   total += venta

#print(f"TOTAL = ${total}")
#print(f"PROMEDIO = ${total/len(ventas)}")
#print(f"Mejor mes = ${max(ventas)}")
#print(f"Peor mes = ${min(ventas)}")
#print("Meses con ventas superiores a $10,000:")
#for i in range(len(ventas)):
    #if ventas[i] > 10000:
        #print(f"Mes {i+1}: ${ventas[i]}")
# ============================================================ Metodo con 2 condiciones ================================================= 

# ============================================================ Metodo con 1 ================================================= 
ventas = [12000, 8500, 15000, 9200, 18000, 11000]
total = 0
enumerate(ventas)
print("Meses con ventas superiores a $10,000:")
for i, venta in enumerate(ventas):
    total += venta
    if venta > 10000:
        
        print(f"Mes {i+1}: ${ventas[i]}")
print(f"TOTAL = ${total}")
print(f"PROMEDIO = ${total/len(ventas):.2f}") #[:.2f] para mostrar solo 2 decimales
print(f"Mejor mes = ${max(ventas)}")
print(f"Peor mes = ${min(ventas)}")
# ============================================================ Metodo con 1 ================================================= 

