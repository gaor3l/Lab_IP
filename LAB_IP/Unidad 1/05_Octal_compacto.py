numero,Octal=12,"" #da valores a numero y Octal
if numero==0: Octal="0" #Da valor a Octal si numero es 0
while numero>0:Octal=str(numero%8)+Octal;numero=numero//8 #Convierte numero a Octal y lo guarda en Octal usando un bucle while
print(Octal) #imprime Octal