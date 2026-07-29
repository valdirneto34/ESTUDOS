from classes import *


def main():

    c1 = Carteira(100)
    c2 = Carteira(300)

    if c1 == c2:
        print("Vocês têm o mesmo valor na carteira!")
    else:
        print("As carteiras têm valores diferentes!")
    print(c1)
    c1 += 200
    print(c1)
    if c1 == c2:
        print("Vocês têm o mesmo valor na carteira!")
    else:
        print("As carteiras têm valores diferentes!")
    c1 -= 50
    print(c1)
    if c1 <= c2:
        print("A segunda carteira tem a mesma quantia ou mais dinheiro!")
    else:
        print("A primeira carteira tem mais dinheiro!")

if __name__ == "__main__":
    main()
