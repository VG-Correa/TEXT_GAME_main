from src.Personagens.Atributos.AtributosMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Personagens.Racas.RacasMD import *

class Personagem:
    def __init__(self, nome, raca:Abstract_Raca, classe:Abstract_Classe):
        
        self.nome = nome
        self.nivel = 0
        self.experiencia = 0
        self.exp_prox_nivel = 100
        
        self.raca = raca
        self.classe = classe
        
    def Rolar_base(self) -> list:
        
        resultado: list[int] = []
        
        for dado in range(6):
            dados = self.raca.dado_base.lancar(6)
            dados = sorted(dados,key=lambda x: x.resultado)[-4:-1]
            soma = dados[0].resultado + dados[1].resultado + dados[2].resultado
            
            resultado.append(soma)    
    
        return resultado         

    def Start_Personagem(self, funcao_atributo):
        
        valores = self.Rolar_base()
        
        op = funcao_atributo(valores)
        self.forca =        Forca(valor=valores[op], 
                                modificador= self.raca.modif_forca_base + self.classe.modif_forca_base)
        valores.pop(op)
        
        op = funcao_atributo(valores)
        valores.pop(op)
        self.destreza =     Destreza(valor=valores[op], 
                                modificador= self.raca.modif_destreza_base + self.classe.modif_destreza_base)
        
        op = funcao_atributo(valores)
        valores.pop(op)
        self.constituicao = Constituicao(valor=valores[op], 
                                modificador= self.raca.modif_constituicao_base + self.classe.modif_constituicao_base)
        
        op = funcao_atributo(valores)
        valores.pop(op)
        self.inteligencia = Inteligencia(valor=valores[op], 
                                modificador= self.raca.modif_inteligencia_base + self.classe.modif_inteligencia_base)
        
        op = funcao_atributo(valores)
        valores.pop(op)
        self.sabedoria =    Sabedoria(valor=valores[op], 
                                modificador= self.raca.modif_sabedoria_base + self.classe.modif_sabedoria_base)
        
        op = funcao_atributo(valores)
        valores.pop(op)
        self.carisma =      Carisma(valor=valores[op], 
                                modificador= self.raca.modif_carisma_base + self.classe.modif_carisma_base)
    
        self.pv = self.classe.rolar_base_vida()[0].resultado + self.constituicao.modificador
        
    def subir_nivel(self):
        resto = self.experiencia - self.exp_prox_nivel
        
        if resto < 0:
            resto = 0
        
        self.nivel += 1
        self.exp_prox_nivel *= 1.10
    
    def __str__(self) -> str:
        return self.nome