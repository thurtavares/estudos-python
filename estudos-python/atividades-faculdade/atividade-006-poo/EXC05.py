from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    email: str


class Agenda:
    def __init__(self):
        self.pessoas = []

    def adicionar(self, pessoa):
        for pessoa_cadastrada in self.pessoas:
            if pessoa_cadastrada.email == pessoa.email:
                print("E-mail já cadastrado!")
                return

        self.pessoas.append(pessoa)
        print("Pessoa adicionada com sucesso!")

    def buscar_por_nome(self, nome):
        resultados = []

        for pessoa in self.pessoas:
            if nome.lower() in pessoa.nome.lower():
                resultados.append(pessoa)

        return sorted(resultados, key=lambda pessoa: pessoa.nome)


agenda = Agenda()

agenda.adicionar(Pessoa("Arthur Tavares", "arthur@email.com"))
agenda.adicionar(Pessoa("Ana Silva", "ana@email.com"))
agenda.adicionar(Pessoa("Carlos Souza", "carlos@email.com"))

# Tentativa de duplicidade
agenda.adicionar(Pessoa("Arthur Oliveira", "arthur@email.com"))

# Busca parcial
resultados = agenda.buscar_por_nome("ar")

print("\nResultados da busca:")

for pessoa in resultados:
    print(f"{pessoa.nome} - {pessoa.email}")