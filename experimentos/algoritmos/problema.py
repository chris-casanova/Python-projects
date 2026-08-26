cadena = "BRACDEFIGHJOKULMNPAQERISTUVWX"  # almacena la cadena de texto

#for idx in range(len(cadena)):
    #print(idx, cadena[idx])

maximalongitud = 0
subcadena = ""
ultimavocal = ""
valdv = 0 #valor de vocal
A = 1
E = 2
I = 3
O = 4
U = 5

voc_a = "" #vocal actual

for char in cadena:
    
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        subcadena += char
        voc_a = char
        print(f"Subcadena: {subcadena}")
        maximalongitud += len(subcadena)
        
    else:
        subcadena = char #OPCIONAL SI NO USAR char directamente en la subcadena, se puede usar char directamente en la subcadena, pero si se quiere almacenar la subcadena completa, se puede usar subcadena = char
        voc_a = char
        
    if voc_a == 'A':
        valdv = A
    elif voc_a == 'E':
        valdv = E
    elif voc_a == 'I':
        valdv = I
    elif voc_a == 'O':
        valdv = O 
    elif voc_a == 'U':
        valdv = U
    else:
        valdv = 0

         
    if ultimavocal == 'A':
        valordeultimavocal = A
    elif ultimavocal == 'E':
        valordeultimavocal = E
    elif ultimavocal == 'I':
        valordeultimavocal = I
    elif ultimavocal == 'O':
        valordeultimavocal = O
    elif ultimavocal == 'U':
        valordeultimavocal = U
    else:
        valordeultimavocal = 0


if voc_a == valordeultimavocal + 1:
    subcadena += char
    valordeultimavocal = voc_a


idx = len(subcadena) - 1
ultimavocal = subcadena[idx]

if valdv == 0:
    subcadena = ""
else:
    subcadena += char

if subcadena:
    print(f"<<<<<<<<<< {subcadena}")

mapa = "AEIOU"

print("La A está en el kilómetro:", mapa.index('A'))
print("La E está en el kilómetro:", mapa.index('E'))
print("La I está en el kilómetro:", mapa.index('I'))
print("La O está en el kilómetro:", mapa.index('O'))
print("La U está en el kilómetro:", mapa.index('U'))


