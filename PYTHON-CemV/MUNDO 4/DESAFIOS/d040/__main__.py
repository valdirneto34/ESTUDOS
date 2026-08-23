from classes import *
from rich import print, inspect


def main():
    u = [
        Usuario("Pedro", "pedro@gmail.com"),
        Usuario("Maria", "maria@hotmail.com")
    ]

    a = [
        Aluno("Cláudia", "ADS", "2 per"),
        Aluno("Ana", "ADM", "4 per"),
        Aluno("Mário", "ADV", "1 per")
    ]

    exportarDadosPersonalizado(XML(), u)
    exportarDadosPersonalizado(JSON(), u)
    exportarDadosPersonalizado(XML(), a)
    exportarDadosPersonalizado(JSON(), a)

    exportarEmPainel(JSON(), a[0])
    exportarEmPainel(XML(), u[1])

    exportarEmPainel(XML(), Aluno("Valdir", "SI", "6 per"))

    exportarDadosPersonalizado(JSON(), Usuario("Carlos", "carlos@outlook.com"))


if __name__ == "__main__":
    main()
