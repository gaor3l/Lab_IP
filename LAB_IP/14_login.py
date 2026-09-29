USUARIO="gaorel"
CLAVE="python123"
usuario=input("usuario: ").strip().lower()
clave=input("contraseña: ")
if usuario==USUARIO and clave==CLAVE:
    print("Bienvenido")
else:
    print("Credenciales incorrectas")