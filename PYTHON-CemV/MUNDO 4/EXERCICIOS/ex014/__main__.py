from classes import *


def main():
    x = Analisador()
    x.analisar(3)
    x.analisar("Valdir")
    x.analisar(8.5)
    x.analisar({"nome": "Valdir", "idade": 22, "sexo": "Masculino"})
    x.analisar(max([6, 9, 3]))
    x.analisar(max([6, 9.3, 3]))
    x.analisar(len([6, 9.3, 3]))


if __name__ == "__main__":
    main()
