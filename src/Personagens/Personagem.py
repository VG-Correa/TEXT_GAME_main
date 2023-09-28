from src.Personagens.Atributos.AtributosMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Personagens.Racas.RacasMD import *


class Membro:
    def __init__(self, nome: str):
        self.nome = nome
        self.equipamento = None
        self.AC = 0 #self.equipamento.AC

class Corpo:
    def __init__(self):
        self.cabeça = None
        self.torax = None
        self.bracos = None
        self.pernas = None
        self.ombro = None
        self.pes = None
        
        self.AC = 0 #Decidir como definir esse valor



class Personagem:
    def __init__(self, nome, raca:Abstract_Raca, classe:Abstract_Classe):
        
        self.nome = nome
        self.nivel = 0
        self.experiencia = 0
        self.exp_prox_nivel = 100
        
        self.raca = raca
        self.classe = classe
        
        self.list_atributos = []
        
        self.pv = None
        self.AC = 0
        
        self.forca = None
        self.list_atributos.append(self.forca)
        
        self.destreza = None
        self.list_atributos.append(self.destreza)
        
        self.constituicao = None
        self.list_atributos.append(self.constituicao)
        
        self.inteligencia = None
        self.list_atributos.append(self.inteligencia)
        
        self.sabedoria = None
        self.list_atributos.append(self.sabedoria)
        
        self.carisma = None
        self.list_atributos.append(self.carisma)
        
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
        
        op = funcao_atributo("Força", valores)
        self.forca =        Forca(valor=valores[op], 
                                modificador_raca= self.raca.modif_forca_base, modificador_classe= self.classe.modif_forca_base)
        valores.pop(op)
        
        op = funcao_atributo("Destreza",valores)
        self.destreza =     Destreza(valor=valores[op], 
                                modificador_raca= self.raca.modif_destreza_base, modificador_classe= self.classe.modif_destreza_base)
        valores.pop(op)
        
        op = funcao_atributo("Constituição",valores)
        self.constituicao = Constituicao(valor=valores[op], 
                                modificador_raca= self.raca.modif_constituicao_base, modificador_classe= self.classe.modif_constituicao_base)
        valores.pop(op)
        
        op = funcao_atributo("Inteligência",valores)
        self.inteligencia = Inteligencia(valor=valores[op], 
                                modificador_raca= self.raca.modif_inteligencia_base, modificador_classe= self.classe.modif_inteligencia_base)
        valores.pop(op)
        
        op = funcao_atributo("Sabedoria",valores)
        self.sabedoria =    Sabedoria(valor=valores[op], 
                                modificador_raca= self.raca.modif_sabedoria_base, modificador_classe= self.classe.modif_sabedoria_base)
        valores.pop(op)
        
        op = funcao_atributo("Carisma",valores)
        self.carisma =      Carisma(valor=valores[op], 
                                modificador_raca= self.raca.modif_carisma_base, modificador_classe= self.classe.modif_carisma_base)
        valores.pop(op)
    
        self.pv = self.classe.rolar_base_vida()[0].resultado + self.constituicao.modificador
        
    def subir_nivel(self):
        resto = self.experiencia - self.exp_prox_nivel
        
        if resto < 0:
            resto = 0
        
        self.nivel += 1
        self.exp_prox_nivel *= 1.10
    
    def Get_descricao_atributos(self):
        print("Atributos do:",self.nome)
        print("Vida:", self.pv)
        print(self.forca)
        print(self.destreza)
        print(self.constituicao)
        print(self.inteligencia)
        print(self.sabedoria)
        print(self.carisma)
        
        pass
    
    def Testar(self, atributo: str, dificuldade: int=0) -> Rolagem:
        atributo: abstract_Atributo = self.__getattribute__(atributo)
        resultado: Rolagem = atributo.testar(DC=dificuldade)
        
        return resultado
    
    def __str__(self) -> str:
        return self.nome