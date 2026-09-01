numero,hexadecimal=255,"" 
if numero==0: hexadecimal="0" 
Hex="0123456789ABCDEF" 
while numero>0:
    residuo=numero%16
    hexadecimal=str(Hex[residuo])+hexadecimal 
    numero=numero//16 
print(hexadecimal) 