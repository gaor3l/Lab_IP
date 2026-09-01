numero,hexadecimal=255,"" #da valores a numero y hexadecimal
if numero==0: hexadecimal="0" #Da valor a hexadecimal si numero es 0
while numero>0: #Inicia un bucle while que se ejecuta mientras numero sea mayor a 0
    residuo=numero%16 #Calcula el residuo de numero entre 16 y lo guarda en residuo
    if residuo==10:residuo="A" #Si residuo es igual a 10, le da el valor de "A" a residuo
    if residuo==11:residuo="B" #Si residuo es igual a 11, le da el valor de "B" a residuo
    if residuo==12:residuo="C" #Si residuo es igual a 12, le da el valor de "C" a residuo
    if residuo==13:residuo="D" #Si residuo es igual a 13, le da el valor de "D" a residuo
    if residuo==14:residuo="E" #Si residuo es igual a 14, le da el valor de "E" a residuo
    if residuo==15:residuo="F" #Si residuo es igual a 15, le da el valor de "F" a residuo
    hexadecimal,numero=str(residuo)+hexadecimal, numero//16 #Convierte numero a hexadecimal y lo guarda en hexadecimal usando un bucle while
print(hexadecimal) #imprime hexadecimal