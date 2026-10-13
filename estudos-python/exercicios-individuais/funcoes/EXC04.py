def dividir(x,y):
    (resultado) = x // y
    resto = x % y
    return resultado, resto


resultado, resto = dividir(10,80)
print(f"A divisão é: ", resultado)
print(f"O resto é: ", resto)