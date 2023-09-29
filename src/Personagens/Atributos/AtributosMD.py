from src.Dados.AbstractDado import *
import math

class abstract_Atributo:
    
    def __init__(self, nome: str, valor: int, modificador_raca: int, modificador_classe: int):
        
        self.modificador_raca = modificador_raca
        self.modificador_classe = modificador_classe
        self.nome = nome
        self.valor = valor
        self.modificador = 0
        self.Update()
        
        self.dado = D20()   
    
    def Update(self):
        self.valor = self.valor + self.modificador_raca
        self.modificador = math.floor(((self.valor - 10) / 2) + self.modificador_classe)
    
    def testar(self, qtd: int=1, DC: int=0):
        return D20().lancar(quantidade=qtd, modificador=self.modificador,DC=DC)[0]
    
    def add(self):
        self.valor += 1
        self.Update()
        return True
    
    def __str__(self):
        descricao =  f"Atributo: {self.nome}\n----> Valor: {self.valor} | Mod: {self.modificador}"
        return descricao
    
        
class Forca(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Força", valor, modificador_raca, modificador_classe)

class Destreza(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Deztreza", valor, modificador_raca, modificador_classe)

class Constituicao(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Constituição", valor, modificador_raca, modificador_classe)

class Inteligencia(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Inteligencia", valor, modificador_raca, modificador_classe)

class Sabedoria(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Sabedoria", valor, modificador_raca, modificador_classe)

class Carisma(abstract_Atributo):
    def __init__(self, valor: int, modificador_raca: int, modificador_classe: int):
        super().__init__("Carisma", valor, modificador_raca, modificador_classe)
