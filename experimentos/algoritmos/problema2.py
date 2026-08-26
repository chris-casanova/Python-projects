#lista corchetes o tupla con parentesis, conjunto con llaves

cadena = "BRACDEFIGHJOKULMNPAQERISTUVWX"  # almacena la cadena de texto

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
        