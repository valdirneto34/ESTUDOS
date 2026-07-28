from hashlib import sha256


class ContaBancaria:
    def __init__(self, id: int, nome: str, saldo: float, chave: str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pedeSenha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo."
        # return f"Estado atual da conta: {self.__dict__}"

    @property
    def nome(self):
        return str(self._titular)

    @nome.setter
    def nome(self, nome: str = None):
        chave = self.pedeSenha()
        if self.validarSenha(chave):
            if len(nome) >= 5:
                self._titular = nome
                print("Mudança de nome \033[1;32mautorizada\033[m!")
        else:
            print("Senha não confere. Mudança de nome \033[1;31mnão autorizada\033[m!")

    def validarSenha(self, chave: str) -> bool:
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def pedeSenha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
            print("Senha curta demais, insira novamente! ", end="")
        return senha

    def sacar(self, valor: float, chave: str = None):
        if chave is None:
            chave = self.pedeSenha()
        if self.validarSenha(chave):
            if valor > self.__saldo:
                print(f"- Saque de R${valor:,.2f} na conta {self._id} \033[1;31mNEGADO\033[m, __saldo insuficiente!")
            elif valor <= 0:
                print(f"- Depósito de R${valor:,.2f} na conta {self._id} \033[1;31mNEGADO\033[m, valor inválido!")
            else:
                self.__saldo -= valor
                print(f"-> Saque de R${valor:,.2f} na conta {self._id} \033[1;32mautorizado\033[m!")
        else:
            print("Senha não confere. Saque \033[1;31mnão autorizado\033[m!")

    def depositar(self, valor):
        if valor <= 0:
            print(f"- Depósito de R${valor:,.2f} na conta {self._id} \033[1;31mNEGADO\033[m, valor inválido!")
        else:
            self.__saldo += valor
            print(f"-> Depósito de R${valor:,.2f} na conta {self._id} \033[1;32mautorizado\033[m!")
