import os

def menuConsulta():
    option = 9999
    while(option != 0):
        print('DIGITE A OPÇÃO DE CONSULTA')
        print('--------------------------------------')


def menuPrincipal():
    option = 0
    while(option != 3):
        print('BEM VINDO AO SISTEMA DE OBSERVAÇÃO DE MANCHAS SOLARES')
        print('------------------------------------------------------')
        print('SELECIONE UMA DAS OPÇÕES NO MENU')
        print('PARA CONSULTAS MENSAIS, OS DADOS VÃO DESDE 1749 ATÉ 2022')
        print('PARA CONSULTAS DIÁRIAS, OS DADOS VÃO DESDE 1818 ATÉ 2022')
        print('***OS GRÁFICOS LEVAM EM CONSIDERAÇÃO OS DADOS DIÁRIOS PARA DETERMINAÇÃO DAS MÉDIAS***')
        print('------------------------------------------------------')
        print('1 - Realizar consulta')
        print('2 - plotar e salvar gráfico a partir de período')
        print('3 - sair')
        option = int(input('Digite a opção desejada:'))
        
if __name__ == '__main__':
    os.system('cls')
    menuPrincipal()