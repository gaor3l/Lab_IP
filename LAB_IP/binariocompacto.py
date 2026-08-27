numero,binario=8,""
if numero==0: binario="0"
while numero>0:binario=str(numero%2)+binario;numero=numero//2
print(binario)