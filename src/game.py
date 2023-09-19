from menu_terminal import Menu_select as ms


# Exemplo de criação do menu
menu = ms.Menu_select(cabeçalho='cabeçalho',texto_seleção = ['negrito','vermelho','azul'])
opt = ['Carregar','Novo Jogo','Opções','Créditos','Sair']
escolha = menu.options(descrição='Essa é a descrição',opções=opt,limite_opçoes=5)

print("\n\nSeleção: ", opt[escolha])