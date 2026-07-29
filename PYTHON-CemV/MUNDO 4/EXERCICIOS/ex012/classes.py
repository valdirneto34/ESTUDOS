from abc import ABC, abstractmethod


class Animal (ABC):
    def __init__(self, nome: str = ""):
        self.nome = nome

    def emitirSom(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som.")


class Pato (Animal):
    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'QUACK! QUACK!'")


class Cachorro (Animal):

    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'AU! AU! AU!'")

class Spitz (Cachorro):

    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'au! au! au! au! au! au! au! au! au!'")

class PitBull (Cachorro):

    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'RUF! RUF! RUF!'")


class Gato (Animal):

    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'MIAU! MIAU!'")


class Galinha (Animal):
    def emitirSom(self):
        print(f"{self.nome} acabou de dizer 'PÓ! PÓ! PÓ!'")
