import random

class Rolagem:
    def __init__(self, nome_dado):
        self.dado = nome_dado
        self.rolagem: int = None
        self.modificador: int = None
        self.resultado: int = None
        self.sobra: int = None
    
    def rolar(self, lados: int, modificador: int) -> str:
        self.rolagem = random.randint(1, lados)
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
                return self.__str__()
                
            elif soma < 1:
                self.resultado = 1
                self.sobra = soma - 1
                return self.__str__()
            
            else:
                self.resultado = soma
                self.sobra = 0
                return self.__str__()
        
    def __str__(self) -> str:
        sinal = "+" if self.modificador >= 0 else ""
        return f"{self.dado}: {self.rolagem}({sinal}{self.modificador}) = {self.resultado} | {self.sobra}"

class Dado:
    def __init__(self, lados: int, nome: str):
        self.nome = nome
        self.lados: int = lados
    
    def lancar(self, quantidade: int =1, modificador:int = 0) -> list[Rolagem]:
        resultados_rolagens: list = []
        
        for i in range(quantidade):
            rolagem = Rolagem(self.nome)
            rolagem.rolar(self.lados,modificador)
            
            resultados_rolagens.append(rolagem)
            
        return resultados_rolagens

class D4(Dado):
    def __init__(self):
        super().__init__(4,'D4')

class D6(Dado):
    def __init__(self):
        super().__init__(6,'D6')

class D8(Dado):
    def __init__(self):
        super().__init__(8,'D8')

class D10(Dado):
    def __init__(self):
        super().__init__(10,'D10')

class D12(Dado):
    def __init__(self):
        super().__init__(12,'D12')

class D20(Dado):
    def __init__(self):
        super().__init__(20,'D20')
