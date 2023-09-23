from Dados.AbstractDado import *

class abstract_Atributo:
    
    def __init__(self, nome, valor, modificador_raca):
        
        self.nome = nome
        self.valor = valor
        self.modificador = (valor - 10 / 2) + modificador_raca
        
        self.dado = D20()
    
    def testar(self):
        return D20().lancar(modificador=self.modificador)[0]
        
class Forca(abstract_Atributo):
    def __init__(self, valor, modificador):
        super().__init__("Força", valor, modificador)

força = Forca(8,-15)

print(força.testar())