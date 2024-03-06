class Animal():
  def __init__(self, nome):
      self.nome = nome

  def som(self):
      pass

class Cachorro(Animal):
    def som(self):
        print("auau")

class Gato(Animal):
    def som(self):
        print("miau")

meu_animal = Cachorro("Salsicha")
meu_animal.som()


meu_animal = Gato('pipi')
meu_animal.som()



