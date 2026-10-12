valor_total = float(input("Valor total em R$ = "))
desconto = float(input("Desconto em porcentagem = "))
desconto_real = 1 - float(desconto / 100)


def descontar(valor_total, desconto_real):
    """ Função para calcular o valor total com desconto."""
    valor = valor_total * desconto_real
    print(f"O total com desconto aplicado é: {valor}")


descontar(valor_total, desconto_real)