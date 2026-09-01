n=int(input("Introduce un numero: "))
primo=1
if n==1:
    primo=0
else:
    i=2
    while i<n:
        if n%i==0:
            primo=0
        i=i+1
if primo==0:
    print("El numero no es primo")
else:
    print("El numero es primo")
    a=0
    b=1
    while a<n:
        c=a+b
        a=b
        b=c
    if a==n:
        print("El numero esta en la serie de Fibonacci")
    else:
        print("El numero no esta en la serie de Fibonacci")
