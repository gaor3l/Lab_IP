edad=18
tiene_credencial=True
Tiene_adeudo=True
if edad >=18:
    es_mayor=True
else: es_mayor=False
if tiene_credencial==True:
    documento_valido=True
Else: documento_valido=False
if Tiene_adeudo==False:
    sin_adeudo=True
else:sin_adeudo=False
if es_mayor and documento_valido and sin_adeudo:
    autorizado=True
else: autorizado=False
print(autorizado)