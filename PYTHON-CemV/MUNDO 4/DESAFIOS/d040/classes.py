import json
import xml.etree.ElementTree as ET
from typing import Union, List
from abc import ABC, abstractmethod

from rich import print as rprint
from rich.panel import Panel


class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


ModelosValidos = Union[Aluno, Usuario, List[Union[Aluno, Usuario]]]

class Formatos(ABC):
    @abstractmethod
    def exportar(self, dados: ModelosValidos) -> str:
            pass


class JSON(Formatos):
    def exportar(self, dados: ModelosValidos) -> str:
        lista_dados = dados if isinstance(dados, list) else [dados]
        lista = [item.__dict__ for item in lista_dados]
        return json.dumps(lista, ensure_ascii=False, indent=2)


class XML(Formatos):
    def exportar(self, dados: ModelosValidos) -> str:
        lista_dados = dados if isinstance(dados, list) else [dados]

        if not lista_dados:
            return ""

        nome_filho = lista_dados[0].__class__.__name__.lower()
        pai = ET.Element("dados")

        for item in lista_dados:
            filho = ET.SubElement(pai, nome_filho)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)

        ET.indent(pai, space="\t")
        return ET.tostring(pai, encoding="unicode", xml_declaration=True)


def exportarDados(formato, dados: ModelosValidos):
    print(formato.exportar(dados))


def exportarDadosPersonalizado(formato: Formatos, dados: ModelosValidos):
    nome_do_formato = formato.__class__.__name__
    cor = "[blue]" if nome_do_formato == "JSON" else "[green]"

    envelopamento = f"{cor}{'=-'*14}  {nome_do_formato}  {'=-'*14}[/]"
    rprint(envelopamento)
    exportarDados(formato, dados)
    rprint(envelopamento)


def exportarEmPainel(formato: Formatos, dados: ModelosValidos):
    nome_do_formato = formato.__class__.__name__

    if isinstance(dados, list):
        nome_da_classe = dados[0].__class__.__name__ if dados else "Vazio"
    else:
        nome_da_classe = dados.__class__.__name__

    titulo = f"{nome_da_classe}: {nome_do_formato}"

    PALETA = {
        ("JSON", "Aluno"): "bold cyan",
        ("JSON", "Usuario"): "bold royal_blue1",
        ("XML", "Aluno"): "bold orange3",
        ("XML", "Usuario"): "bold red3",
    }

    cor = PALETA.get((nome_do_formato, nome_da_classe), "white")
    
    txt = formato.exportar(dados)
    
    from rich import box
    painel = Panel(txt, title=titulo, width=100, border_style=cor, box=box.DOUBLE)
    rprint(painel)
