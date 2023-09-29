from src.Personagens.Personagem import Personagem
from src.Personagens.Racas.RacasMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Itens.Equipamentos.Armas.Espada_madeira import Espada_Madeira
from src.Itens.Equipamentos.Armaduras.Corpo.Peitoral_ferro import Peitoral_Ferro

def return0(atributo, opcoes):
    return 0

Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(return0)
Victor.Get_descricao_atributos()

espada = Espada_Madeira()
capacete = Peitoral_Ferro()

Victor.Equipar_mao_esquerda(espada)

print("="*20)
Rato = Personagem("Rato", Rato(), Guerreiro(), [Espada_Madeira()])
Rato.Start_Personagem(return0)
Rato.Get_descricao_atributos()

print("="*40)
ataque = Victor.Usar_HabilidadeAtaque("Soco","mao_esquerda",Rato)[0]
print(ataque)