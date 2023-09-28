from config.settings import CONFIG_RARIDADE

class Raridade:
    def __init__(self, nome):
        self.nome = nome
        self.chance = CONFIG_RARIDADE[nome]["chance"]
        self.poder = CONFIG_RARIDADE[nome]["poder"]
        
    def __str__(self):
        return self.nome

class Equipamento:
    def __init__(self, nome: str, tipo: str, membro: str, AC: int, radidade: Raridade):
        self.nome = nome
        self.tipo = tipo
        self.membro = membro
        self.AC = AC
        
        self.raridade = radidade