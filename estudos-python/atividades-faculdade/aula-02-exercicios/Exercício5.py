nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

resultado = (nota1 + nota2 + nota3) / 3

print("Média para ser aprovado = 7.0")
print("Sua média = ", resultado)
if resultado >= 7:
    print("Resultado = Aprovado")
if not (resultado) >= 7:
    print("Resultado = Não Aprovado")
