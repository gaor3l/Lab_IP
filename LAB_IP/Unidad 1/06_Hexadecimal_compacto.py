numero,hexadecimal=255,""
if numero==0: hexadecimal="0"
while numero>0:
    residuo=numero%16
    if residuo==10:residuo="A"
    if residuo==11:residuo="B"
    if residuo==12:residuo="C"
    if residuo==13:residuo="D"
    if residuo==14:residuo="E"
    if residuo==15:residuo="F"
    hexadecimal,numero=str(residuo)+hexadecimal, numero//16
print(hexadecimal)