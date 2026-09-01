numero,hexadecimal=255,"" #da valores a numero y hexadecimal
if numero==0: hexadecimal="0" #Da valor a hexadecimal si numero es 0
while numero>0: #Inicia un bucle while que se ejecuta mientras numero sea mayor a 0
residuo=numero%16 #Calcula el residuo de numero entre 16 y lo guarda en residuo
    if residuo==10:residuo="A" elif residuo==11:residuo="B" elif residuo==12:residuo="C" elif residuo==13:residuo="D" elif residuo==14:residuo="E" elif residuo==15:residuo="F" #Convierte el residuo a su equivalente hexadecimal si es mayor o igual a 10
    hexadecimal,numero=str(residuo)+hexadecimal, numero//16 #Concatena residuo con hexadecimal y divide numero entre 16
print(hexadecimal) #imprime hexadecimal