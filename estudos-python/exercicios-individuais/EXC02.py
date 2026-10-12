lista = input("Digite uma sequência de números separados por espaços: ")
numeros = list(map(int, lista.split()))

for numero in numeros:
    if (numero % 2 == 0):
        print(f"{numero} é par!")
    else:
        print(f"{numero} é impar!")