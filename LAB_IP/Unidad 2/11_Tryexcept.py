while True:
    try:
        edad = int(input("edad: "))
        if 0 <= edad <= 120:
            break

        print("La edad debe estar entre 0 y 120.")
    except ValueError:
        print("Escribe un numero entero")

print(f"edad registrada: {edad}")