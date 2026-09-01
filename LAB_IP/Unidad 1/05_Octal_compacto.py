numero,Octal=12,""
if numero==0: Octal="0"
while numero>0:Octal=str(numero%8)+Octal;numero=numero//8
print(Octal)