from src.Dados.AbstractDado import *
from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Personagens.Atributos.AtributosMD import abstract_Atributo

class AbstractHabilidade_ataque:
    def __init__(self, nome: str, tipo_dano: str, dado_base: Dado, dado_dano_base: Dado, atributo_base: str, qtd_ataques:int = 1):
        self.nome = nome
        self.tipo_dano = tipo_dano
        self.dado_base = dado_base
        self.dado_dano_base = dado_dano_base
        self.atributo_base = atributo_base
        self.qtd_ataques = qtd_ataques
    
    def Atacar(self, Ator, equipamento: AbstractEquipamento,  alvo):
        atributo: abstract_Atributo = Ator.__getattribute__(self.atributo_base)
        mod_equipamento = equipamento.dado.lancar(1)[0].resultado
        rolagens: [Rolagem] = self.dado_base.lancar(self.qtd_ataques, DC=alvo.AC,modificador=atributo.modificador + mod_equipamento)
        return rolagens
    
    def Dano(self, Ator, equipamento: AbstractEquipamento=None):
        atributo: abstract_Atributo = Ator.__getattribute__(self.atributo_base)
        mod_equipamento = equipamento.dado.lancar(1)[0].resultado
        return self.dado_dano_base.lancar(1, modificador=atributo.modificador + mod_equipamento)

class Soco(AbstractHabilidade_ataque):
    def __init__(self):
        super().__init__(nome="Soco", tipo_dano="fisico", dado_base=D20(),dado_dano_base=D4(),atributo_base="forca", qtd_ataques=1)
        