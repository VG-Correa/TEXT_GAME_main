import sys
import os
import time
from menu_terminal import os_terminal_controller as ostc

TERMINAL = ostc.Os_Terminal_Controller()
        
class Menu_select:
    def __init__(self,cabeçalho,
                 limite_opçoes=10,
                 texto_seleção = ['negrito','vermelho','cinza'],
                 texto_padrao = ['normal','branco','normal']):
        
        self.limite_opçoes = limite_opçoes
        self.cabeçalho = cabeçalho

        self.estilo_texto = {
            'normal':'0',
            'negrito':'1',
            'sublinhado':'4',
            'negativo':'7',
        
        }

        self.cor_texto = {
            'branco':'30',
            'vermelho':'31',
            'verde':'32',
            'amarelo':'33',
            'azul':'34',
            'roxo':'35',
            'ciano':'36',
            'cinza':'37',
            'normal':''}

        self.cor_fundo = {
            'branco':'40',
            'vermelho':'41',
            'verde':'42',
            'amarelo':'43',
            'azul':'44',
            'roxo':'45',
            'ciano':'46',
            'cinza':'47',
            'normal':''}

        self.texto_seleção = ''
        self.texto_padrao = ''
        self.texto_normal = '\033[m'
        self.Set_Paleta(texto_seleção,texto_padrao)

    def Set_Paleta(self,texto_seleção = ['bold','vermelho','branco'],
                   texto_padrao = ['normal','normal','normal']):
        
        self.texto_seleção = '\033[' + self.estilo_texto[texto_seleção[0]] + ';' + self.cor_texto[texto_seleção[1]] + ';' + self.cor_fundo[texto_seleção[2]] + 'm'
        self.texto_padrao = '\033[' + self.estilo_texto[texto_padrao[0]] + ';' + self.cor_texto[texto_padrao[1]] + ';' + self.cor_fundo[texto_padrao[2]] + 'm'

    def options(self,cabeçalho='',descrição='',opções=[],limite_opçoes=0):
        TERMINAL.hide_cursor()
        
        cabeçalho = self.cabeçalho if cabeçalho == '' else cabeçalho
        descrição = descrição
        opções = opções
        limite_opçoes = self.limite_opçoes if limite_opçoes == 0 else limite_opçoes
        qtd_opçoes = len(opções)
        menor = 0
        ultimo = qtd_opçoes - 1

        menor_sessao = 0
        maior_sessao = limite_opçoes-1

        if maior_sessao > qtd_opçoes:
            maior_sessao = qtd_opçoes-1

        index_selecionado = 0
        
        while True:
            TERMINAL.clear()
            print(cabeçalho)
            print('\n' + descrição + '\n')

            for index, opção in enumerate(opções):

                if index == index_selecionado:
                    print(self.texto_seleção + str(opção) + self.texto_normal)

                else:
                    if index >= menor_sessao and index <= maior_sessao:
                        print(self.texto_padrao + str(opção) + self.texto_normal)

            key = TERMINAL.ReadKey()
            if key == 'KeyUp':
                index_selecionado -= 1
            elif key == 'KeyDown':
                index_selecionado += 1
            elif key == 'Enter':
                TERMINAL.show_cursor()
                return index_selecionado
            
            if index_selecionado < 0:
                index_selecionado = ultimo
                maior_sessao = ultimo
                menor_sessao = ultimo - limite_opçoes +1
               
            elif index_selecionado > ultimo:
                index_selecionado = 0
                maior_sessao = limite_opçoes-1
                menor_sessao = 0
            
            if index_selecionado < menor_sessao:
                menor_sessao -= 1
                maior_sessao -= 1
            
            elif index_selecionado > maior_sessao:
                maior_sessao += 1
                menor_sessao += 1
            
# menu = Menu_select(cabeçalho='cabeçalho',texto_seleção = ['negrito','vermelho','verde'])
# print(menu.options(descrição='Essa é a descrição',opções=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))