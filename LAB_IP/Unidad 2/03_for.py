for numero in range(0, 7,2):
    cuadrado = numero ** 2
    print(numero, cuadrado)
#for con listas
materias=["python","linux","interfaces"]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}: {materia}")

for materia in materias:
    print(materia)

cadena = "0123456789ABCDEF"
for letra in cadena:
        print(letra)

for i in range(len(cadena)):
    print(cadena[i])    