class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido!\n")

        self.__saldo += valor
        print("Deposito concluído!\n")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido!\n")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente!\n")

        self.__saldo -= valor
        print("Saque concluído!\n")

    def extrato(self):
        print(f"Titular: {self.titular}.")
        print(f"Saldo atual: R$ {self.__saldo:.2f}.\n")

conta = ContaBancaria("Arthur", 1000)

conta.extrato()
conta.depositar(200)
conta.sacar(100)
conta.extrato()
conta.sacar(0)