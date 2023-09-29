from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Dados.AbstractDado import D6
from src.Itens.Equipamentos.Raridades.Comum import Comum
from src.Itens.Equipamentos.Encantamentos.Normal import Normal

class Peitoral_Ferro(AbstractEquipamento):
    def __init__(self):
        super().__init__("Peitoral de Ferro", "armadura", "torax", D6(), 5, Comum(), Normal())