amostras = int(input("Digite a quantidade de amostras: "))
capacidade = int(input("Digite a capacidade de cada bandeja: "))

bandejas_completas = amostras // capacidade
restantes = amostras % capacidade

print(bandejas_completas)
print(restantes)