from src.Itens.Equipamentos.Encantamentos.Aspecto_flamejante import Aspecto_FlamejanteI
from src.Itens.Equipamentos.Raridades.Incomum import Incomum
from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Personagens.Personagem import Personagem
from src.Personagens.Racas.RacasMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Itens.Equipamentos.Armas.Espada_madeira import Espada_Madeira
from src.Itens.Equipamentos.Armaduras.Corpo.Peitoral_ferro import Peitoral_Ferro

random.seed(1)

def return0(atributo, opcoes):
    return 0
# random.seed(645112)

Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(return0)
Victor.Get_descricao_atributos()

espada = Espada_Madeira()
capacete = Peitoral_Ferro()

# print("AC: ", Victor.AC)
Victor.Equipar_mao_esquerda(espada)
Victor.Equipar_armadura(capacete)
# print("AC: ", Victor.AC)

rato = Personagem("Rato gosmento",Rato(),Guerreiro(),DROPS_equip=[Espada_Madeira,Peitoral_Ferro])
rato.Start_Personagem(return0)
rato.Get_descricao_atributos()

ataque = Victor.Usar_HabilidadeAtaque("Soco","mao_esquerda",rato)[0].teste
ataque = Victor.Usar_HabilidadeAtaque("Soco","mao_esquerda",rato)[0]
print(ataque)

if ataque.teste:
    rato.Dar_dano(Victor.Get_habilidade_ataque("Soco").Dano(Victor,equipamento=Victor.corpo.mao_esquerda.equipamento)[0].resultado,"normal", "fisico")
    rato.Dar_dano(Victor.Get_habilidade_ataque("Soco").Dano(Victor,equipamento=Victor.corpo.mao_esquerda.equipamento)[0].resultado,"normal", "fisico")
    
print(rato.pv)
