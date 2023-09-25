from src.Dados.AbstractDado import *

class abstract_Atributo:
    
    def __init__(self, nome: str, valor: int, modificador: int):
        
        self.nome = nome
        self.valor = valor + modificador
        self.modificador = (valor - 10) / 2
        print(self.nome, valor, self.modificador, modificador)
        
        self.dado = D20()
    
    def testar(self):
        return D20().lancar(modificador=self.modificador)[0]
    
        
class Forca(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Força", valor, modificador)

class Destreza(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Deztreza", valor, modificador)

class Constituicao(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Constituição", valor, modificador)

class Inteligencia(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Inteligencia", valor, modificador)

class Sabedoria(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Sabedoria", valor, modificador)

class Carisma(abstract_Atributo):
    def __init__(self, valor: int, modificador: int):
        super().__init__("Carisma", valor, modificador)
