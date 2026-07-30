from classes import *
from rich import print, inspect


def main():
    p1 = PIX()
    p1.valor = 2_684_321.76
    print(f"Valor formatado: {p1.fvalor}")

    finalizarPagamento(Boleto(), 6_999.90)
    finalizarPagamento(Credito(), 59.89)
    finalizarPagamento(PIX(), 8_500)
    finalizarPagamento(PIX(), -49.99)


if __name__ == "__main__":
    main()
