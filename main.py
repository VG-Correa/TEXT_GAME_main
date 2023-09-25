from src.Personagens.Personagem import *
from src.menu_terminal.menu_terminal import *

menu = Menu_select("Testando")


def Escolher_Atributo(opcoes:list):
    print(opcoes)
    escolha = menu.options(opcoes)
    return escolha
    

Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(Escolher_Atributo)