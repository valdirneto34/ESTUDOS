from rich import print


class Diario:
    def __init__(self, senhamestra="Tricia!@"):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        print("[green]Diário LIBERADO![/]")
        for segredo in self.__segredos:
            print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, novaSenha):
        senhaAtual = input(str("Digite a senha atual para concluir a alteração: ")).strip()
        if self.__senha != senhaAtual:
            raise PermissionError("Senha atual \033[1;31mincorreta\033[m!")
        else:
            self.__senha = novaSenha.strip()