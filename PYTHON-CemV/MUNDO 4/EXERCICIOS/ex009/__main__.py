from ex009 import Avaliacao
from rich import print, inspect

def main():
   av1 = Avaliacao("Valdir", "Redes de Computadores 2", 95.4)
   av1.setNota(-235)
   print(f"{av1.nome} tirou {av1.getNota()} em {av1.disciplina}.")
   inspect(av1, private=True)

if __name__ == "__main__":
    main()