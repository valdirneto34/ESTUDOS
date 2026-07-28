from abc import ABC, abstractmethod
from datetime import date

class Pessoa (ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido!")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self):
        raise PermissionError("Você não pode alterar a idade! Mude o ano de nascimento.")


class Aluno (Pessoa) :

    cursosOficiais = ["ADM", "ADS", "ENG", "CONT", "SI"]

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso: str):
        if curso in Aluno.cursosOficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais!")

    def addCurso(self, curso: str):
        curso = curso.strip().upper()
        if curso in self.cursosOficiais:
            raise ValueError(f"Nome {curso} já está incluso nos Cursos!")
        if 2 <= len(curso) <= 5:
            self.cursosOficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} está fora do padrão para Cursos!")