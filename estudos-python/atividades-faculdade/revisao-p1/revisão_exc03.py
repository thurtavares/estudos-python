def selecionar(valores, regra):
    return list(filter(regra, valores))

valores = [12, 28, 30, 55, 70, 91]

maiores_iguais_70 = lambda valor: valor >= 70
menores_30 = lambda valor: valor < 30

print(selecionar(valores, maiores_iguais_70))
print(selecionar(valores, menores_30))