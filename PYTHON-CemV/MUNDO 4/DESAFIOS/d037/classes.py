from rich import print
from rich.panel import Panel


class Mensagem:

    def __init__(self, msg: str = "", tipo: str = "Aviso", icone: str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    @property
    def titulo(self):
        return f"{self._icone} {self._tipo.upper()} {self._icone}"

    def mostrar(self):
        msg = Panel(self._mensagem, title=self.titulo, style="#ffffff on #000000", width=50)
        print(msg)


class Alerta (Mensagem):

    def __init__(self, msg = ""):
        super().__init__(msg, "Alerta", ":warning:")

    def mostrar(self):
        msg = Panel(self._mensagem, title=self.titulo, style="#000000 on #FFFC1B", width=50)
        print(msg)


class Erro (Mensagem):

    def __init__(self, msg = ""):
        super().__init__(msg, "Erro", ":prohibited:")

    def mostrar(self):
        msg = Panel(self._mensagem, title=self.titulo, style="#ffff00 on #880000", width=50)
        print(msg)
