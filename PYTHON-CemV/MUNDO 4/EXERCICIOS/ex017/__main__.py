from classes import *


def main():
    a = Numero(200)
    b = Texto("Gafanhoto")
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    tenteDobrar(a)
    tenteDobrar(b)
    tenteDobrar(c)
    tenteDobrar(d)
    tenteDobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == "__main__":
    main()
