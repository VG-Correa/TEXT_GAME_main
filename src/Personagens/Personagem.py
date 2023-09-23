from Atributos.AbstractAtributo import abstract_Atributo

class Personagem:
    def __init__(self, nome, raca, classe):
        
        self.nome = nome
        self.forca = "Classe Atr_Forca"
        self.destreza = "Classe Atr_Destreza"
        self.constituicao = "Classe Atr_Constituicao"
        self.inteligencia = "Classe Atr_Inteligencia"
        self.sabedoria = "Classe Atr_Sabedoria"
        self.carisma = "Classe Atr_Carisma"
        
        self.raca = raca
        self.classe = classe
    
    
    def __str__(self) -> str:
        return self.nome
    
Victor = Personagem("Victor")
print(Victor)