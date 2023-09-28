from src.Personagens.Personagem import *
from src.menu_terminal.menu_terminal import *

menu = Menu_select("Vida: 100")


def Escolher_Atributo(Atributo: str, opcoes:list):
    
    descicao = f"Escolha o valor para o atributo:\n{Atributo}"
    
    escolha = menu.options(opções=opcoes, descrição=descicao)
    return escolha
    
    # return escolha
    
Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(Escolher_Atributo)
Victor.Get_descricao_atributos()
print(Victor.Testar('forca',12))
print(Victor.Testar('destreza',12))
