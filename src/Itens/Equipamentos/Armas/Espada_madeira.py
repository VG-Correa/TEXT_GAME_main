from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Dados.AbstractDado import D4
from src.Itens.Equipamentos.Raridades.Comum import Comum
from src.Itens.Equipamentos.Encantamentos.Normal import Normal
from src.Itens.Equipamentos.Encantamentos.Aspecto_flamejante import Aspecto_FlamejanteI

class Espada_Madeira(AbstractEquipamento):
    def __init__(self):
        super().__init__(nome="Espada de Madeira", 
                         tipo="arma", 
                         membro="uma_mao", 
                         AC=1,
                         dado=D4(),
                         radidade=Comum(),
                         auto_encantamento=True,
                         pool_encantamentos= [Normal, Aspecto_FlamejanteI])