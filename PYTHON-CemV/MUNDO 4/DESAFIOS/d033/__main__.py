from diagramaDeClasses import *
from rich import print, inspect


def main():

    try:
        a1 = Aluno("Valdir", 2400, "SI")
    except Exception as e:
        print(f"Ocorreu um erro de {type(e).__name__}: {e}")

    try:
        a1 = Aluno("Valdir", 2004, "ADV")
    except Exception as e:
        print(f"Ocorreu um erro de {type(e).__name__}: {e}")

    a1 = Aluno("Valdir", 2004, "SI")

    try:
        a1.addCurso("MEDICINA")
    except Exception as e:
        print(f"Ocorreu um erro de {type(e).__name__}: {e}")

    try:
        a1.addCurso("ADS")
    except Exception as e:
        print(f"Ocorreu um erro de {type(e).__name__}: {e}")


    a2 = Aluno("Patrícia", 2005, "ADS")
    a2.addCurso("MED")
    print(f"Aluno 1: {a1.__dict__}")
    print(f"Aluno 2: {a2.__dict__}")
    print(f"Cursos: {a1.cursosOficiais}")
    # inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()
