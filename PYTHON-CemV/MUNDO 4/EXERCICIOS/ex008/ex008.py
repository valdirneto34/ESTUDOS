class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f"--- Conta {self.id} criada com sucesso. __Saldo atual de {self.__saldo:,.2f} ---")

    def __str__(self):
        # return f"A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo."
        return f"Estado atual da conta: {self.__dict__}"
    
    def depositar(self, valor):
        if valor <= 0:
            print(f"- Depósito de R${valor:,.2f} na conta {self.id} \033[1;31mNEGADO\033[m, valor inválido!")
        else:
            self.__saldo += valor
            print(f"-> Depósito de R${valor:,.2f}  na conta {self.id} \033[1;32mautorizado\033[m!")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f"- Saque de R${valor:,.2f} na conta {self.id} \033[1;31mNEGADO\033[m, saldo insuficiente!")
        elif valor <= 0:
            print(f"- Depósito de R${valor:,.2f} na conta {self.id} \033[1;31mNEGADO\033[m, valor inválido!")
        else:
            self.__saldo -= valor
            print(f"-> Saque de R${valor:,.2f}  na conta {self.id} \033[1;32mautorizado\033[m!")
