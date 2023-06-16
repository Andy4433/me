#Busquei desenvolver um projeto simples e de fácil implementação ao assistir alguns vídeos de programação.
#Durante essa pesquisa, encontrei um projeto interessante e decidi tentar implementá-lo por conta própria corrigindo
#caso tenha feito algum erro. 
#Eu vi esse projeto e me interressei em reproduzi-lo, ele é feito em python e importa a biblioteca PySimpleGUI

import PySimpleGUI as sg  # Importa a biblioteca PySimpleGUI com o alias sg

def criar_nova_tarefa():
    sg.theme('DarkBlue4')  # Define o tema da janela como 'DarkBlue4', podemos definir varias paletas de cores podem ser: 'DefaultNoMoreNagging',
#'GreenTan','Dark','DarkAmber','DarkBlue','DarkBlue2','DarkBlue3','DarkBlue4','DarkBrown','DarkBrown2','DarkBrown3','DarkGrey','DarkGrey2','DarkGrey3',
#'DarkGrey4','DarkPurple','DarkPurple2','DarkPurple3','DarkPurple4','LightGreen','LightGreen2','LightGreen3','LightGreen4','LightGrey','LightGrey2',
#'LightGrey3','LightGrey4','LightRed','LightRed2','LightRed3'e'LightRed4'.Essas são apenas algumas das opções disponíveis. 
    linha = [
        [sg.Checkbox(' '), sg.Input(' ')]  # Cria uma linha com um Checkbox e um Input
    ]
    layout = [
        [sg.Frame('tarefas', layout=linha, key='container')],  # Cria um frame chamado 'tarefas' contendo a linha criada anteriormente
        [sg.Button('nova tarefa'), sg.Button('resetar')]  # Cria dois botões: 'nova tarefa' e 'resetar'
    ]
    return sg.Window('TODO LIST', layout=layout, finalize=True)  # Retorna uma janela com o título 'TODO LIST' e o layout criado

janela = criar_nova_tarefa()  # Chama a função criar_nova_tarefa para criar a janela inicial

while True:
    event, values = janela.read()  # Lê os eventos e valores da janela
    if event == sg.WINDOW_CLOSED:  # Se o evento for o fechamento da janela
        break  # Encerra o loop
    elif event == 'nova tarefa':  # Se o evento for 'nova tarefa'
        janela.extend_layout(janela['container'], [[sg.Checkbox(' '), sg.Input(' ')]])  # Adiciona uma nova linha com Checkbox e Input na janela
    elif event == 'resetar':  # Se o evento for 'resetar'
        janela.close()  # Fecha a janela atual
        janela = criar_nova_tarefa()  # Cria uma nova janela chamando a função criar_nova_tarefa

