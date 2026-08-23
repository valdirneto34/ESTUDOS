from classes import *
from rich import print, inspect
from rich.panel import Panel


def main():
    painel = Panel("", title="Carrinho", width=50)
    p1 = Produto("Mouse", 325)
    p2 = Produto("Teclado", 433)
    p3 = Produto("Memória 256", 2_799.90)
    p4 = Produto("Placa de Vídeo", 16_999)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p3 + p4

    c2 = c2 + c1 + p2

    painel.renderable = str(c1)
    print(painel)
    painel.renderable = str(c2)
    print(painel)


if __name__ == "__main__":
    main()
