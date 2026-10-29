def contar_caracteres(frase):
    contagem = {}
    for caractere in frase:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

frase = "ola mundo"
print(contar_caracteres(frase))
print("Total de caracteres:", len(frase))
