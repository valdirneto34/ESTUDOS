class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    def getNota(self):
        return self._nota

    def setNota(self, valor):
        if 0 <= valor <= 100:
            self._nota = valor
        else:
            print(f"Nota {valor} \033[1;31minválida\033[m!")
