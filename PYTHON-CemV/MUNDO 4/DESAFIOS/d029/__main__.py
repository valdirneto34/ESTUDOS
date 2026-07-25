from diario import *
from rich import print, inspect


def main():
    d = Diario("Gafanhoto")

    d.escrever("Primeira mensagem")
    d.escrever("Você é uma pessoa simpática")
    d.escrever("Você gosta de Python")


    d.senha = "Love"

    try:
        d.ler("Gafanhoto")
    except Exception as e:
        print(f"[red]ERRO: {e}[/]")

    try:
        d.ler("Love")
    except Exception as e:
        print(f"[red]ERRO: {e}[/]")

    #inspect(d, private=True)

if __name__ == "__main__":
    main()
