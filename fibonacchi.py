#print("dame un numero entero positivo:"); n = int(input())
n = int(input("dame un numero entero positivo: "))

if isinstance(n, int) and n >= 0:
    x = 0 
    o = 1
    for i in range(n):
        print(o , end=" ")
        o = x + o
        x = o - x 
        
else:
    print("ERROR: El numero ingresado no es un entero positivo")
    