
ventas= [12000, 8500, 15000, 9200, 18000]

while True:
    try:


        search_value = input("Ingrese el valor que desea buscar en la lista de ventas o \"q\" para salir: ")
        
        if search_value.lower() == "q":
            break
        found = False #variable bandera

        for i in ventas:
            if i == int(search_value):
                found = True

        if found:
            print(f"El valor {search_value} existe en la posición #{ventas.index(int(search_value))+1}")
        else:
            print(f"El valor {search_value} no existe en la lista.")

        print()


    except ValueError:
        print("ERROR: solo numeros enteros positivos")

