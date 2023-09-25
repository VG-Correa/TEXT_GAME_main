from src.Dados.AbstractDado import Dado
from src.Dados.AbstractDado import *
from config.settings import CONFIG_CLASSES

class Abstract_Classe:

    def __init__(self, nome: str, dado_vida: Dado):
        self.nome = nome
        self.dado_vida = dado_vida
        
        self.modif_forca_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["forca_base"]
        self.modif_destreza_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["destreza_base"]
        self.modif_constituicao_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["constituicao_base"]
        self.modif_inteligencia_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["inteligencia_base"]
        self.modif_sabedoria_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["sabedoria_base"]
        self.modif_carisma_base = CONFIG_CLASSES[nome]["Modificadores_atributos"]["carisma_base"]
    
        
        self.prof_armas = []
        self.prof_armaduras = []
        
    def rolar_base_vida(self):
        return self.dado_vida.lancar(1)     
    
class Guerreiro(Abstract_Classe):
    def __init__(self):
        super().__init__("Guerreiro", D10())