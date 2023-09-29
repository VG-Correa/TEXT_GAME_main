from config.settings import CONFIG_RARIDADE
from src.Dados.AbstractDado import *
from src.Itens.Equipamentos.Raridades.AbstractRaridade import AbstractRaridade
from src.Itens.Equipamentos.Encantamentos.AbstractEncantamento import AbstractEncantamento


class AbstractEquipamento:
    def __init__(self, nome: str, 
                 tipo: str, 
                 membro: str, 
                 dado: Dado, 
                 AC: int, 
                 radidade: AbstractRaridade, 
                 encantamento: AbstractEncantamento):
        
        self.nome = nome
        self.tipo = tipo
        self.membro = membro
        self.dado = dado
        self.AC = AC
        self.encantamento = encantamento
        self.raridade = radidade
        self.equipado: bool = False
        
    def __str__(self):
        return self.nome
        
    def testar_dano(self,proficiencia_arma: int=0, proficiencia_elemento: int=0):
        dano_base = self.dado.lancar(1, proficiencia_arma + self.raridade.poder)
        enc = self.encantamento.dado.lancar(1,proficiencia_elemento + self.encantamento.raridade.poder)
        return dano_base[0] + enc[0]
