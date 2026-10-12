nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
aulas_totais = int(input("Quantas aulas tiveram em todo o semestre?: "))
faltas = int(input("Quantas faltas você teve?: "))

media = (nota1 + nota2) / 2
frequencia = ((aulas_totais - faltas) / aulas_totais) * 100

aprovado = (media >= 6) and (frequencia >= 75)

print(aprovado)
