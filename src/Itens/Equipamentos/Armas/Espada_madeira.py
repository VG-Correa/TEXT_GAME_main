from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Dados.AbstractDado import D4
from src.Itens.Equipamentos.Raridades.Comum import Comum
from src.Itens.Equipamentos.Encantamentos.Normal import Normal

class Espada_Madeira(AbstractEquipamento):
    def __init__(self):
        super().__init__(nome="Espada de Madeira", 
                         tipo="arma", 
                         membro="uma_mao", 
                         AC=1,
                         dado=D4(),
                         radidade=Comum(),
                         encantamento=Normal())