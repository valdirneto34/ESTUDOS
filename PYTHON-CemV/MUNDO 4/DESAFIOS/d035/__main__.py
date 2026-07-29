from classes import *
from rich import print, inspect


def main():

    a1 = DOC("Prova", 250_000)
    a2 = PDF("Contrato", 1_300_234)

    abrirArquivo(a1)
    abrirArquivo(a2)


if __name__ == "__main__":
    main()
