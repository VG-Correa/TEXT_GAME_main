from src.Dados.AbstractDado import *

from config.settings import CONFIG_RACAS


class Abstract_Raca:

    def __init__(self, nome: str, dado_base: Dado):
        
        self.nome = nome
        self.dado_base = dado_base
        
        self.modif_forca_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["forca_base"]
        self.modif_destreza_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["destreza_base"]
        self.modif_constituicao_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["constituicao_base"]
        self.modif_inteligencia_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["inteligencia_base"]
        self.modif_sabedoria_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["sabedoria_base"]
        self.modif_carisma_base = CONFIG_RACAS[nome]["Modificadores_atributos"]["carisma_base"]
        self.modif_AC = CONFIG_RACAS[nome]["Modificadores_atributos"]["AC"]
        
        
        self.prof_armas = []
        self.prof_armaduras = []
      
class Humano(Abstract_Raca):
    def __init__(self):
        super().__init__("Humano", D6())
        
class Rato(Abstract_Raca):
    def __init__(self):
        super().__init__("Rato", D4())
        