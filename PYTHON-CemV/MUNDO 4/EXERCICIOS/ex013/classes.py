class Mae:
    def __init__(self, nome: str = "Mamãe"):
        self.nome = nome

    def fazerPudim(self):
        print(f"{self.nome} faz PUDIM com leite condensado e calda!")

    def fritarCoxinha(self):
        print(f"{self.nome} frita COXINHA no oléo de soja!")


class Filha (Mae):

    def fazerPudim(self):
        print(f"{self.nome} faz PUDIM com Leite Ninho com Nutella!")


class Filho (Mae):

    def fritarCoxinha(self):
        print(f"{self.nome} frita COXINHA na Air Fryer!")
