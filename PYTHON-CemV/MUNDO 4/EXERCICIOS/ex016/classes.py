class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta.")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ.")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separe as partes sobre uma frigideira.")

class Pedra:
    pass

def tentarAbrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir um objeto do tipo {objeto.__class__.__name__}")