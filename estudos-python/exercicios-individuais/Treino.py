valor_produtos = (input("Digite o valor dos produtos, em R$: "))
produtos = list(map(float, valor_produtos.split()))

media = sum(produtos) / len(produtos)
soma = sum(produtos)

print(f"O valor total dos produtos é: R$ {soma}")
print(f"A média do valor dos produtos é: R$ {media}")

produtos_ordenados = sorted(produtos, reverse=True)

print(f"Produtos do maior para o menor em R$: {produtos_ordenados}")