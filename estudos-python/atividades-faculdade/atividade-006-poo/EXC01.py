class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} --- {self.autor}({self.ano})"

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano < 0:
            raise ValueError("O ano não pode ser negativo")

        self.__ano = novo_ano


livro1 = Livro("Dom Casmurro", "Machado de Asssis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
# livro3 = Livro("Erro", "TesteErro", -2026)

print(livro1)
print(livro2)
# print(livro3)