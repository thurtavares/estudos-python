from abc import ABC, abstractmethod


class Entidade(ABC):

    @property
    @abstractmethod
    def id(self):
        pass


class Produto(Entidade):

    def __init__(self, id, nome, preco):
        self._id = id
        self.nome = nome
        self.preco = preco

    @property
    def id(self):
        return self._id


class Repositorio:

    def __init__(self):
        self.dados = {}

    def adicionar(self, entidade):
        if entidade.id in self.dados:
            print("ID já cadastrado!")
            return

        self.dados[entidade.id] = entidade
        print("Produto adicionado!")

    def obter(self, id):
        return self.dados.get(id)

    def remover(self, id):
        if id not in self.dados:
            print("Produto não encontrado!")
            return

        del self.dados[id]
        print("Produto removido!")

    def listar(self):
        return list(self.dados.values())


repositorio = Repositorio()

produto1 = Produto(1, "Notebook", 3500)
produto2 = Produto(2, "Mouse", 150)
produto3 = Produto(3, "Teclado", 250)

repositorio.adicionar(produto1)
repositorio.adicionar(produto2)
repositorio.adicionar(produto3)

produto = repositorio.obter(1)

if produto:
    print(f"\nProduto encontrado: {produto.nome}")

print("\nProdutos cadastrados:")

for produto in repositorio.listar():
    print(f"{produto.id} - {produto.nome} - R$ {produto.preco:.2f}")

print("\nRemovendo produto:")
repositorio.remover(2)

print("\nLista atualizada:")

for produto in repositorio.listar():
    print(f"{produto.id} - {produto.nome} - R$ {produto.preco:.2f}")