from classes import *
from rich import print, inspect


def main():
    m1 = Mensagem("Olá, Mundo!")
    m1.mostrar()
    print()

    m1 = Alerta("Cuidado! Cuidado! Ele está voltando!")
    m1.mostrar()
    print()

    m1 = Erro("Operação impossível!")
    m1.mostrar()
    print()


if __name__ == "__main__":
    main()
