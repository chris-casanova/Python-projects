list= [12000, 8500, 15000, 9200, 18000]
found = False #variable bandera
for i in list:
    if i == 9200:
        print(F"El valor {i} existe en la lista y se encuentra en la posición #{list.index(i)} ")
        found = True
        break
    else:
        found = False
        print(f"El valor {i} no existe en la lista.")