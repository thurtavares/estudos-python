import random

def adivinhar_numero():
    numero = random.randint(1, 10)
    palpite = int(input("Adivinhe um número de 1 a 10: "))
    if palpite == numero:
        print("Acertou!")
    else:
        print("Errou! O número era", numero)

adivinhar_numero()
