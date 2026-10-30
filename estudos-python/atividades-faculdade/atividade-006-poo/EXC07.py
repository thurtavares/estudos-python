from datetime import datetime


class RegistravelMixin:

    def log(self, mensagem):
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{horario}] [{self.__class__.__name__}] {mensagem}")


class Pedido(RegistravelMixin):

    def __init__(self, numero):
        self.numero = numero
        self.status = "Criado"

        self.log(f"Pedido {self.numero} criado.")

    def pagar(self):
        if self.status != "Criado":
            self.log("Não foi possível realizar o pagamento.")
            return

        self.status = "Pago"
        self.log(f"Pedido {self.numero} pago.")

    def cancelar(self):
        if self.status == "Cancelado":
            self.log("O pedido já está cancelado.")
            return

        if self.status == "Pago":
            self.log("Não é possível cancelar um pedido pago.")
            return

        self.status = "Cancelado"
        self.log(f"Pedido {self.numero} cancelado.")


pedido = Pedido(101)

pedido.pagar()
pedido.cancelar()