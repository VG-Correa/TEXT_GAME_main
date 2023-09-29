from src.Dados.AbstractDado import *
from src.Itens.Equipamentos.Raridades.AbstractRaridade import AbstractRaridade
from src.Itens.Equipamentos.Raridades.Comum import Comum


class AbstractEncantamento:
    def __init__(self, nome: str, dado: Dado=D0(), raridade: AbstractRaridade=Comum(), elemento="normal"):
        self.nome = nome
        self.dado = dado
        self.raridade = raridade
        self.elemento = elemento
    
    def __str__(self):
        return self.nome