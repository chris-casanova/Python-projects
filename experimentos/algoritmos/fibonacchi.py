while True:
    try:
        #print("dame un numero entero positivo:"); n = int(input())
        entrada = input("dame un numero entero positivo (o 'exit' para salir): ")
        
        if entrada.lower() == "exit":
            break
        
        n = int(entrada)
        
        if isinstance(n, int) and n > 0:
            x = 0 
            o = 1
            for i in range(n):
                print(o , end=" ")
                o = x + o
                x = o - x
            print()
            
        else:
            print("ERROR: solo numeros enteros positivos")
    except ValueError:
        print("ERROR: solo numeros enteros positivos")
    