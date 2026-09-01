numero,binario=8,""        #da valores a numero y binario
if numero==0: binario="0"  #Da valor a binario si numero es 0
while numero>0:binario=str(numero%2)+binario;numero=numero//2 #Convierte numero a binario y lo guarda en binario usando un bucle while
print(binario) #imprime binario