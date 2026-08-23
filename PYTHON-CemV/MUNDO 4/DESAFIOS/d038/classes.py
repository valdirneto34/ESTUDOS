class Carrinho:
    def __init__(self, produtos: list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = "\n".join(str(p) for p in self.produtos)
        return f"{itens}{linha}\nTotal: {formataDinheiro(self.total)}"
        

    def __iadd__(self, produto: Produto):
        self.produtos.append(produto)
        return self

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho")


class Produto:
    def __init__(self, nome: str, preco: float = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({formataDinheiro(self.preco)})"


def formataDinheiro(valor: float):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)
