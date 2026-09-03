#for numero in range(2,101):
#    divisores = 0
#    for divisor in range(2,numero):
#        if numero % divisor == 0:
#            divisores += 1
#    if divisores == 0:
#        print(numero)
for numero in range(1,101,2):
  if numero == 2 or numero == 3 or numero == 5 or numero == 7: print(numero)
  elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0: print(numero)