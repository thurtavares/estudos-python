class Produto:
    aliquota = 0.10

    def __init__(self,nome,preco,codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

    def preco_final(self):
        return self.preco * (1 + Produto.aliquota)

    @classmethod
    def mudar_aliquota(cls, nova_aliquota):
        cls.aliquota = nova_aliquota

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented

        return self.codigo == outro.codigo

produto1 = Produto("Notebook", 4000, 1)
produto2 = Produto("Notebook Gamer", 6000, 1)
produto3 = Produto("Televisão", 10000, 3)

print("Preço inicial:")
print(f"{produto1.nome}: R$ {produto1.preco_final():.2f}")

Produto.mudar_aliquota(0.20)

print("\nPreço final:")
print(f"{produto1.nome}: R$ {produto1.preco_final():.2f}")

print(f"\nComparação dos produtos:")
print(produto1 == produto2)
print(produto2 == produto3)