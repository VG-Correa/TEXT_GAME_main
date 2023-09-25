from src.Personagens.Personagem import *
from src.menu_terminal.menu_terminal import *

menu = Menu_select("Testando")


def Escolher_Atributo(dado_base: Dado):
    
    dados = dado_base.lancar(4)
    dados = sorted(dados,key=lambda x: x.resultado)[-4:-1]
    soma = dados[0] + dados[1] + dados[2]
    
    return soma    
    

Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(Escolher_Atributo)