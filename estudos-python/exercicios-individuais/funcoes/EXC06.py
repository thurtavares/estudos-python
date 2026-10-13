def externa():
    def interna():
        return "Funcionou"

    return interna()

print(externa())