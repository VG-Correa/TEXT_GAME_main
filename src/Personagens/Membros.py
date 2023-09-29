from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento

class Membro:
    def __init__(self, nome: str):
        self.nome = nome
        self.equipamento = None
        self.AC = 0 #self.equipamento.AC
        self.ocupado = False
    
    def Equipar(self, equipamento: AbstractEquipamento):
        if self.ocupado == False:
            self.equipamento = equipamento
            self.AC = self.equipamento.AC
            self.equipamento.equipado = True
            self.ocupado = True
            return True
        else:
            return False
    
    def Desequipar(self):
        if self.equipamento != None:
            self.equipamento = None
            self.AC = 0
            self.equipamento.equipado = False
            self.ocupado = False
            return True
        else:
            return False

class Cabeca(Membro):
    def __init__(self):
        super().__init__("cabeca")

class Torax(Membro):
    def __init__(self):
        super().__init__("torax")

class Bracos(Membro):
    def __init__(self):
        super().__init__("bracos")

class Mao_esquerda(Membro):
    def __init__(self):
        super().__init__("mao_esquerda")

class Mao_direita(Membro):
    def __init__(self):
        super().__init__("mao_direita")

class Ombro(Membro):
    def __init__(self):
        super().__init__("ombro")

class Maos(Membro):
    def __init__(self):
        super().__init__("maos")

class Pernas(Membro):
    def __init__(self):
        super().__init__("pernas")

class Pes(Membro):
    def __init__(self):
        super().__init__("pes")