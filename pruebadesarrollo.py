# Solo pares
# Parte 1
def pares(n):
    for i in range(0, n*2, 2):
        print(i)

x = pares(10)

    #Se recorrieron todos los números pares(se sumo de dos en dos), entre el 0 y el número otorgado (n) multiplicado por 2, 
    # puesto que sería el límite real del recorrido. 


# Parte 2
def paresNo0(n):
    for i in range(2, n*2+2, 2):
        print(i)

x = paresNo0(4)

    #Se recorrieron todos los números pares(se sumo de dos en dos), entre el 0 y el número otorgado (n) multiplicado por 2+2, 
    # puesto que sería el límite real del recorrido, sin considerar al 0.


# Suma impares
# Parte 1
def sumImpares(n):
    s = 0
    for i in range(1, n, 2):
        # print(i)
        s += i
    print(s)

x = sumImpares(6)

    #Se recorrieron todos los números impares(se sumo de dos en dos), entre el 1 (no es necesario partir del 0, por ser par) 
    # y el número otorgado (n). Se sumó cada uno de estos números, para obtener el resultado. 


# Parte 2
def sumIntervalo(min, max):
    s = 0
    for i in range(min, max, 1):
        if i%2 == 1:
            # print(i)
            s += i
    print(s)

x = sumIntervalo(6, 30)

    #Se recorrieron todos los números que estan dentro del rango establecido por el min y el max. Si el número iterado era impar,
    #se añadió a la suma.|


#Secuencia de Fibonacci
def Fibonacci(n):
    if n < 2: 
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def Fib(n):
    for i in range(n):
        print(Fibonacci(i))
    print(Fibonacci(n))

x = Fib(7)


    # La primera función se llama a si misma, para obtener los valores que dan como resultado el valor de Fibonacci para "n".
    # La segunda función recorre la secuencia para imprimir cada uno de los números hasta llegar al valor de Fibonacci para "n".
