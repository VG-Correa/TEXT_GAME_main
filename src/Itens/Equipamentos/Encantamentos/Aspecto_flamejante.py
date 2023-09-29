from src.Dados.AbstractDado import D4
from src.Itens.Equipamentos.Encantamentos.AbstractEncantamento import *

class Aspecto_FlamejanteI(AbstractEncantamento):
    def __init__(self):
        super().__init__("Aspecto Flamejante I", D4(), Comum())