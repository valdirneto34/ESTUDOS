from classes import *
from rich import print, inspect


def main():

    f = Designer("Ana", 12_000)

    try:
        f.salario = 5_000
    except Exception as e:
        print(f"Houve um erro do tipo {type(e).__name__}: {e}")

    funcionarios = [
        Desenvolvedor("Pedro", 18_000),
        Designer("José", 25_000),
        Gerente("Mariana", 45_000)
    ]

    for f in funcionarios:
        print(f)


if __name__ == "__main__":
    main()
