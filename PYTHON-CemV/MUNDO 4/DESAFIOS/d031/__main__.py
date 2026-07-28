from retangulo import *
from rich import print, inspect


def main():

    r = Retangulo()

    try:
        r.base = -12
        r.altura = 33
    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

    r.medidas = (9, 3)

    print(r.medidas)

    # inspect(r, private=True, methods=True)


if __name__ == "__main__":
    main()
