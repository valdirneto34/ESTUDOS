from abc import ABC, abstractmethod


class Arquivo (ABC):

    def __init__(self, nome: str, ext: str, tam: int):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext

    @property
    def nomeCompleto(self):
        return f"'{self.nome}.{self._extensao}'({self.tamanho/1_000_000:.2f}MB)"

    @property
    def extensao(self):
        return self._extensao

    @nomeCompleto.setter
    def nomeCompleto(self, nome):
        pass

    @extensao.setter
    def extensao(self, ext: str):
        formatos = ["doc", "docx", "pdf"]
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo está em um formato não suportado!")

    @abstractmethod
    def abrir(self):
        pass


class PDF (Arquivo):

    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nomeCompleto} no Adobe Reader!")


class DOC (Arquivo):

    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "docx", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nomeCompleto} no Microsoft Word!")

def abrirArquivo(arq):
    arq.abrir()