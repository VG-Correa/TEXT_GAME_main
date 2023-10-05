from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Dados.AbstractDado import D6
from src.Itens.Equipamentos.Raridades.Comum import Comum
from src.Itens.Equipamentos.Encantamentos.Normal import Normal
from src.Itens.Equipamentos.Encantamentos.Aspecto_flamejante import Aspecto_FlamejanteI

class Peitoral_Ferro(AbstractEquipamento):
    def __init__(self):
        super().__init__("Peitoral de Ferro", "armadura", "torax", D6(), 2, Normal(),auto_encantamento=True,pool_encantamentos=[Normal, Aspecto_FlamejanteI])