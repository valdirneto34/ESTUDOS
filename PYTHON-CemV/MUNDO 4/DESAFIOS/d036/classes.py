from abc import ABC, abstractmethod
import locale


class Pagamento (ABC):

    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor >= 0:
            self._valor = valor
        else:
            raise ValueError("O pagamento só pode ser efetuado para valores positivos!")

    @property
    def fvalor(self):
        return locale.currency(self.valor, grouping=True, symbol=True, international=False)

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto (Pagamento):

    def pagar(self, valor: float):
        self.valor = valor


class Credito (Pagamento):

    def pagar(self, valor: float):
        self.valor = valor


class PIX (Pagamento):

    def pagar(self, valor: float):
        self.valor = valor


def finalizarPagamento(tipoPag: Pagamento, valor: float):
    try:
        tipoPag.pagar(valor)
        print(f"Pagamento \033[1;32mCONFIRMADO\033[m de {tipoPag.fvalor} via {tipoPag.__class__.__name__}!")
    except Exception as e:
        print(f"\033[1;31mFalha\033[m de pagamento de {locale.currency(valor, grouping=True)} via {tipoPag.__class__.__name__}!")
