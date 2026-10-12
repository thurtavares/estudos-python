nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_aprovado = 6.0
reprovado = 3.0


media = (nota1 + nota2 + nota3) / 3
if media >= media_aprovado:
    print(f"Sua média foi {media}, você está aprovado!")

if (media >= 3)and(media < 6):
    print(f"Sua média foi {media}, você está de recuperação!")

if media < 3:
    print(f"Sua média foi {media}, você está reprovado!")