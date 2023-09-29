import random
import math

class Rolagem:
    def __init__(self, nome_dado: str, DC: int=0):
        self.dado = nome_dado
        self.rolagem: int = None
        self.modificador: int = None
        self.resultado: int = None
        self.sobra: int = None
        self.DC = DC
        self.teste = None
    
    def rolar(self, lados: int, modificador: int) -> str:
        if lados > 0:
            self.rolagem = random.randint(1, lados)
        else:
            self.rolagem = 0
            
        self.modificador = modificador
        
        soma = self.rolagem + self.modificador
        
        if modificador == lados:
            self.resultado = lados
            self.sobra = soma - lados
            
        elif modificador == lados*-1:
            self.resultado = 1
            self.sobra = soma - 0
            
        else:
            
            if soma > lados:
                self.resultado = lados
                self.sobra = soma - lados
                
            elif soma < 1:
                self.resultado = 1
                self.sobra = soma - 1
            
            else:
                self.resultado = soma
                self.sobra = 0
        
        if self.resultado >= self.DC:
            self.teste = True
        else:
            self.teste = False
    
    def __add__(self, outra_rolagem):
        nov_DC = math.floor((self.DC + outra_rolagem.DC)/2)
        nov_modificador: int = self.modificador + outra_rolagem.modificador
        nov_resultado: int = self.resultado + outra_rolagem.resultado
        nov_sobra: int = self.sobra + outra_rolagem.sobra
        nov_rolagem = self.rolagem + outra_rolagem.rolagem
        

        if nov_resultado >= nov_DC:
            nov_teste = True
        else:
            nov_teste = False
        
        Rolagem_nov = Rolagem(nome_dado=f"{self.dado}_+_{outra_rolagem.dado}",DC=nov_DC)
        Rolagem_nov.modificador = nov_modificador
        Rolagem_nov.resultado = nov_resultado
        Rolagem_nov.rolagem = nov_rolagem
        Rolagem_nov.teste = nov_teste
        Rolagem_nov.sobra = nov_sobra
        
        Rolagem_nov.__setattr__("termo_01", self)
        Rolagem_nov.__setattr__("termo_02", outra_rolagem)
        
        return Rolagem_nov        
    
    def __str__(self) -> str:
        sinal = "+" if self.modificador >= 0 else ""
        return f"{self.dado:<4}: {self.rolagem:<3}({sinal:}{self.modificador:^3}) = {self.resultado:<3} | {self.sobra:<3}\n --> DC-{self.DC} | Teste: {self.teste}"

class Dado:
    def __init__(self, lados: int, nome: str):
        self.nome: str = nome
        self.lados: int = lados
    
    def lancar(self, quantidade: int = 1, modificador:int = 0, DC: int = 0) -> list[Rolagem]:
        resultados_rolagens: list[Rolagem] = []
        
        for i in range(quantidade):
            rolagem = Rolagem(nome_dado=self.nome, DC=DC)
            rolagem.rolar(self.lados,modificador)
            
            resultados_rolagens.append(rolagem)
            
        return resultados_rolagens

    def __str__(self):
        return self.nome
    
class D0(Dado):
    def __init__(self):
        super().__init__(0,"D0")

class D4(Dado):
    def __init__(self):
        super().__init__(4,"D4")

class D6(Dado):
    def __init__(self):
        super().__init__(6,"D6")

class D8(Dado):
    def __init__(self):
        super().__init__(8,"D8")

class D10(Dado):
    def __init__(self):
        super().__init__(10,"D10")

class D12(Dado):
    def __init__(self):
        super().__init__(12,"D12")

class D20(Dado):
    def __init__(self):
        super().__init__(20,"D20")

class D100(Dado):
    def __init__(self):
        super().__init__(100,"D100")
        

