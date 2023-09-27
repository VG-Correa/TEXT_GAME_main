from src.Personagens.Personagem import *
from src.menu_terminal.menu_terminal import *

menu = Menu_select("Vida: 100")

opc = ["Carregar Jogo", "Novo Jogo", "Sair"]

escolha = menu.options(opções=opc)




# def Escolher_Atributo(opcoes:list):
    
#     escolha = menu.options(opções=opcoes)
#     return escolha
    
# Victor = Personagem("Victor", Humano(), Guerreiro())
# Victor.Start_Personagem(Escolher_Atributo)