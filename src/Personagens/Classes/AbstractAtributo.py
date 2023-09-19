from abc import ABC, abstractmethod

class abstract_Atributo(ABC):
    
    @abstractmethod
    def __init__(self):
        
        self.nome = "Nome do atributo"
        self.valor = None
        self.modificador = None
    
    @abstractmethod
    def set_valor(self, valor):
        self.valor = valor