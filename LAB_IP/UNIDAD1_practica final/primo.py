n=int(input("introduce un numero: "))
i=2
primo=1
while i<n:
    if n%i==0:
        primo=0
    i=i+1
if n==1:
    print("El numero 1 no es primo")
elif primo==1:
    print("El numero es primo")
else:
    print("El numero no es primo")