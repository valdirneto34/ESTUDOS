from ex010 import Avaliacao
from rich import print, inspect

def main():
   av1 = Avaliacao("Valdir", "Redes de Computadores 2")
   av1.nota = 91.6
   av1.nota = -7.2
   print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}.")
   # inspect(av1, private=True)

if __name__ == "__main__":
    main()