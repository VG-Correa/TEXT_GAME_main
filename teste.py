from src.Itens.Equipamentos.Encantamentos.Aspecto_flamejante import Aspecto_FlamejanteI
from src.Itens.Equipamentos.Raridades.Incomum import Incomum
from src.Itens.Equipamentos.AbstractEquipamento import AbstractEquipamento
from src.Personagens.Personagem import Personagem
from src.Personagens.Racas.RacasMD import *
from src.Personagens.Classes.ClassesMD import *
from src.Itens.Equipamentos.Armas.Espada_madeira import Espada_Madeira
from src.Itens.Equipamentos.Armaduras.Corpo.Peitoral_ferro import Peitoral_Ferro

def return0(atributo, opcoes):
    return 0
# random.seed(645112)

Victor = Personagem("Victor", Humano(), Guerreiro())
Victor.Start_Personagem(return0)
Victor.Get_descricao_atributos()

espada = Espada_Madeira()
capacete = Peitoral_Ferro()

Victor.Equipar_mao_esquerda(espada)
