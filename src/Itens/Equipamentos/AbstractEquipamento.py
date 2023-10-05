from config.settings import CONFIG_RARIDADE
from src.Dados.AbstractDado import *
from src.Itens.Equipamentos.Raridades.AbstractRaridade import AbstractRaridade
from src.Itens.Equipamentos.Encantamentos.AbstractEncantamento import AbstractEncantamento
from src.Itens.Equipamentos.Encantamentos.Normal import Normal


class AbstractEquipamento:
    def __init__(self, nome: str, 
                 tipo: str, 
                 membro: str, 
                 dado: Dado, 
                 AC: int, 
                 radidade: AbstractRaridade, 
                 encantamento: AbstractEncantamento=None,
                 auto_encantamento: bool = False,
                 pool_encantamentos = None
                 ):
        
        self.nome = nome
        self.tipo = tipo
        self.membro = membro
        self.dado = dado
        self.AC = AC
        self.encantamento = Normal()
        self.raridade = radidade
        self.equipado: bool = False
        self.pool_encantamentos = pool_encantamentos
        
        if auto_encantamento and encantamento == None:
            self.encantar()
        elif auto_encantamento and encantamento != None:
            self.encantar(encantamento)
        elif auto_encantamento == False and encantamento != None:
            self.encantar(encantamento)
        
        
    def __str__(self):
        return self.nome
        
    def testar_dano(self,proficiencia_arma: int=0, proficiencia_elemento: int=0):
        dano_base = self.dado.lancar(1, proficiencia_arma + self.raridade.poder)
        enc = self.encantamento.dado.lancar(1,proficiencia_elemento + self.encantamento.raridade.poder)
        return dano_base[0] + enc[0]

    def encantar(self, encantamento:AbstractEncantamento=None, forcar = False):
        # Forçar quando verdadeiro, força o encantamento do item mesmo que ele esteja fora da pool de encantamentos possíveis do item
        
        if encantamento != None:
            if forcar:
                self.__encantar(encantamento)
            else:
                for enc in self.pool_encantamentos:
                    if enc.nome == encantamento.nome:
                        self.__encantar(encantamento)
                        return True
                    
        else:
            for encantamento in self.pool_encantamentos:
                encantamento = encantamento()
                raridade = encantamento.raridade
                chance = raridade.chance
                sorteio = random.randint(0,1000)/1000
                
                if chance > sorteio:
                    self.__encantar(encantamento)
                    return True
                
    
    def __encantar(self, encantamento: AbstractEncantamento):
        self.encantamento = encantamento
    