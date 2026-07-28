from contaBancaria import *
from rich import print, inspect

def main():
    print("---------- CONTA BANCÁRIA ----------")
    nome = str(input("==> Digite o nome do titular: "))
    valor = float(input("==> Digite o valor do depósito inicial: "))
    print("==> Digite a sua ", end="")

    cc = ContaBancaria(123, nome, valor)
    while True:
        print("============ MENU ============")
        print("1 - SACAR")
        print("2 - DEPOSITAR")
        print("3 - MUDAR NOME")
        print("4 - INFORMAÇÕES DA CONTA")
        print("5 - ENCERRAR")
        print("============ MENU ============")
        opc = str(input("Digite sua opção: "))
        if opc == "1":
            valor = float(input("==> Digite o valor para o saque: "))
            cc.sacar(valor)
        elif opc == "2":
            valor = float(input("==> Digite o valor para o depósito: "))
            cc.depositar(valor)
        elif opc == "3":
            novoNome = str(input("==> Digite o novo nome: "))
            cc.nome = novoNome
        elif opc == "4":
            print(cc)
        elif opc == "5":
            print(f"Encerrando sessão. Até mais {cc.nome.split()[0]}!")
            break
        else:
            print("\nOpção inválida! Tente outra.\n")
    print("---------- CONTA BANCÁRIA ----------") 

if __name__ == "__main__":
    main()