while True:
    edad = input("edad: ")
    if edad.isdigit():
        edad = int(edad)
        if 0 <= edad <= 120:
            break
        print("La edad debe estar entre 0 y 120.")
    else:
        print("Escribe un numero entero")
print(f"edad registrada: {edad}")