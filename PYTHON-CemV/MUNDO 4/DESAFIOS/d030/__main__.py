from credencial import *
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = "Gafanhoto"
    print(c.senha)

    c.validar("Trix!@")
    c.validar("Gafanhoto")
    
    # inspect(c, private=True, methods=True)

if __name__ == "__main__":
    main()