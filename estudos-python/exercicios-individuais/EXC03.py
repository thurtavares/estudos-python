password = "SenhaExemplo123"
tentativa = 0
limite = 5

while tentativa < limite:
    senha = input("Digite a senha: ")
    if senha == password:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente!\n")
        tentativa += 1

        if tentativa == limite:
            print("Tentativas máximas atingidas.\nAcesso bloqueado!")
