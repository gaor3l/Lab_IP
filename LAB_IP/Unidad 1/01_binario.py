numero=8
binario=""
if numero==0:
    binario="0"
while numero>0:
    binario=str(numero%2)+binario
    numero=numero//2
print(binario)  #imprime binario

