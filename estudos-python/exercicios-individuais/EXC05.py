precos = input("Digite o preço de 5 produtos, separe utilizando um espaço e digite apenas os números! :")

numeros = list(map(float, precos.split()))
media = (sum(numeros)) / 5
soma = sum(numeros)

print(f"O valor total é: R$ {soma}.")
print(f"A média dos valores é: R$ {media}.")

for numero in numeros:
    if numero > 100:
        print(f"R$ {numero} custam mais de R$ 100,00")