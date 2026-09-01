numero=12
octal=""
if numero==0:
    octal="0"
while numero>0:
    octal=str(numero%8)+octal
    numero=numero//8
print(octal)