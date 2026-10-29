def substituir_vogais(texto, caractere):
    for vogal in "aeiouAEIOU":
        texto = texto.replace(vogal, caractere)
    return texto

texto = "Programacao em Python"
print(texto)
print(substituir_vogais(texto, "*"))
