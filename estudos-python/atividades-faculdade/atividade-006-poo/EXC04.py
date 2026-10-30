class Animal:
    def falar(self):
        print("Um animal faz barulho.")

class Cachorro(Animal):
    def falar(self):
        super().falar()
        print("O cachorro late.\n")

class Gato(Animal):
    def falar(self):
        super().falar()
        print("O gato mia.\n")

def chamar_animais(animais):
        for animal in animais:
            animal.falar()


cachorro = Cachorro()
gato = Gato()

lista_animais = [cachorro, gato]

chamar_animais(lista_animais)