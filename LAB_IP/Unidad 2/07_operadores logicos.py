edad=19
tiene_credencial=True
Tiene_adeudo=True
es_mayor=edad>=18
documento_valido=tiene_credencial
sin_adeudo=not Tiene_adeudo
autorizado=es_mayor and documento_valido or sin_adeudo
print(autorizado)