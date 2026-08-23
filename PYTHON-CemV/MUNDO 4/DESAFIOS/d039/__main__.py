from classes import *
from rich import print, inspect


def main():
    validarDado(Usuario(), "valdirneto34")
    validarDado(Email(), "valdirneto100c@gmail.com")
    validarDado(Email(), "valdir.neto@empresa.com.br")
    validarDado(Senha(), "V@ld1r&n3t0")


if __name__ == "__main__":
    main()
