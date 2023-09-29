from config.settings import CONFIG_RARIDADE
from src.Itens.Equipamentos.Raridades.AbstractRaridade import AbstractRaridade


class Comum(AbstractRaridade):
    def __init__(self):
        super().__init__("Comum")
