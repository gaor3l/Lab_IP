cuentatotal=int(input("Ingrese la cuenta total"))
porcentajepropina=int(input("Ingrese el porcentaje de propina"))
propina=cuentatotal*porcentajepropina/100
n=int(input("Ingrese el número de personas"))
print("Cuenta con propina: ", float(cuentatotal+propina))
montopp=float(cuentatotal+propina)/n
print("Monto por persona: ", f"{montopp:.2f}")
