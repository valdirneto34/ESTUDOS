from abc import ABC, abstractmethod
import re


class Validador(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def validar(self, valor: str) -> bool:
        pass


class Usuario(Validador):
    def validar(self, valor) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Email(Validador):
    def validar(self, valor) -> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Senha(Validador):
    def validar(self, valor) -> bool:
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


def validarDado(validador: Validador, valor: str):
    from rich import print
    resultado = validador.validar(valor)
    print(f" Valor: '[yellow]{valor}[/]' é válido para [blue]{validador.__class__.__name__}[/]? {'[green]SIM' if resultado else '[red]NÃO'}[/]")
