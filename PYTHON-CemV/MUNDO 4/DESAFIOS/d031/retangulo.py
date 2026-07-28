class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("O valor da base deve ser um número!")
        if base <= 0:
            raise ValueError("Valor inválido para a base!")
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError("O valor da altura deve ser um número!")
        if altura <= 0:
            raise ValueError("Valor inválido para a altura!")
        self._altura = altura

    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("Área não pode ser configurada desse jeito!")

    @property
    def medidas(self):
        return f"Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @medidas.setter
    def medidas(self, medidas:tuple):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas em formato de tupla!")
        if len(medidas) != 2:
            raise SyntaxError("Informe uma tupla com apenas  dois valores numéricos!")
        if isinstance(medidas[0], float) or isinstance(medidas[0], int):
            self.base = medidas[0]
        else:
            raise TypeError("A base deve ser um número!")
        if isinstance(medidas[1], float) or isinstance(medidas[1], int):
            self.altura = medidas[1]
        else:
            raise TypeError("A base deve ser um número!")
