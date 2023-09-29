from src.Personagens.Atributos.AtributosMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Personagens.Racas.RacasMD import *
from src.Personagens.Membros import *
from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Personagens.Habilidades.AbstractHabilidade import *

class Corpo:
    def __init__(self):
        self.cabeça = Cabeca()
        self.ombro = Ombro()
        self.torax = Torax()
        self.bracos = Bracos()
        self.pernas = Pernas()
        self.pes = Pes()
        self.mao_esquerda = Mao_esquerda()
        self.mao_direita = Mao_direita()
        
        self.AC = 0
    
    def Equipar(self, membro: str, equipamento: AbstractEquipamento):
        membro = self.__getattribute__(membro).Equipar(equipamento)
        return membro

class Personagem:
    def __init__(self, nome, raca:Abstract_Raca, classe:Abstract_Classe, DROPS:list = []):
        
        self.nome = nome
        self.nivel = 0
        self.experiencia = 0
        self.exp_prox_nivel = 100
        self.corpo = Corpo()
        self.habilidades_ataque: [AbstractHabilidade_ataque] = [Soco()]
        self.habilidades_defesa = []
        self.itens = []
        self.fraqueza_elemental = []
        self.vantagem_elemental = []
        self.fraqueza_ataque = []
        self.vantagem_ataque = []
        
        self.status_efeito = []
        
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
        
        self.DROPS = DROPS
        
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
        self.AC = self.raca.modif_AC + self.classe.modif_AC + self.destreza.modificador
        
        
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
    
    def Equipar_armadura(self, Equipamento: AbstractEquipamento) -> bool:
        if Equipamento.tipo == "armadura":
            equip = self.corpo.Equipar(Equipamento.membro, Equipamento)
            return equip
        else:
            return False
    
    def Equipar_mao_esquerda(self, Equipamento: AbstractEquipamento):
        if Equipamento.tipo == "arma" and Equipamento.membro == "uma_mao":
            equip = self.corpo.Equipar("mao_esquerda", Equipamento)
            return equip
        else:
            return False
    
    def Equipar_mao_direita(self, Equipamento: AbstractEquipamento):
        if Equipamento.tipo == "uma_mao":
            self.corpo.Equipar("mao_direita", Equipamento)
            return True
        else:
            return False
        
    def Equipar_duas_maos(self, Equipamento: AbstractEquipamento):
        if Equipamento.tipo == "duas_maos":
            self.corpo.mao_esquerda.Equipar(Equipamento)
            self.corpo.mao_direita.Equipar(Equipamento)
            return True
        else:
            return False
    
    def Usar_HabilidadeAtaque(self,habilidade_nome:str, mao: str, alvo):
        
        for habilidade in self.habilidades_ataque:
            if habilidade.nome == habilidade_nome:
                habilidade: AbstractHabilidade_ataque = habilidade
                
                arma: AbstractEquipamento = self.corpo.__getattribute__(mao).equipamento
                if arma != None:
                    testes = habilidade.Atacar(self, arma, alvo)
                    return testes
                
    
    def __str__(self) -> str:
        return self.nome