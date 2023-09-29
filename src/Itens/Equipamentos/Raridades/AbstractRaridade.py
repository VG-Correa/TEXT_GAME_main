from config.settings import CONFIG_RARIDADE

class AbstractRaridade:
    def __init__(self, nome: str):
        self.nome = nome
        self.chance = CONFIG_RARIDADE[nome]["chance"]
        self.poder = CONFIG_RARIDADE[nome]["poder"]
        
    def __str__(self):
        return self.nome
