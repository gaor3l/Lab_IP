MAX=3
for intento in range(1, MAX+1):
    usuario=input("usuario: ")
    clave=input("contraseña: ")
    if usuario=="gaorel" and clave=="python123":
        print("Bienvenido")
        break
    else:
        print("Acceso bloqueado")