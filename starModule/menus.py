import os
import sys 
from configparser import ConfigParser
import platform
from starModule import starFunctions

#CONFIGURING DAILY AND MONTHLY DICTS
#----------------------------------------------------------------------------------------
DAILY = starFunctions.populateByDay('./byDayCsv.csv')
MONTHLY = starFunctions.populateByMonth('./byMonthCsv.csv')
#----------------------------------------------------------------------------------------

#--------------------------------------------------------------
#configuring root dir
ROOT_DIR = os.path.dirname(os.path.abspath("config.py"))
os.chdir(ROOT_DIR)
#--------------------------------------------------------------

#CONFIGURING CLEAR COMMAND
#----------------------------------------------------------------------------------------
configuration = ConfigParser()
configuration.read('config.ini')
CLEAR_COMMAND = configuration['CLEAR'][platform.system()]
#----------------------------------------------------------------------------------------

#-----------------------------------------------------------------
def maxMinMean(mode):
    os.system(CLEAR_COMMAND)

    start = int(input('Digite o ano de início: '))
    end = int(input('digite o ano final da consulta: '))

    if(start < 1749 or end > 2022 or start > end):
        while(start < 1749 or end > 2022 or start > end):
            os.system(CLEAR_COMMAND)
            print('Os anos selecionados estão fora do range de anos')
            print('Digite anos entre 1818 e 2022')
            start = int(input('Digite o ano de início: '))
            end = int(input('digite o ano final da consulta: '))
            
    os.system(CLEAR_COMMAND)
    print('No intervalo dado, os resultados foram os seguintes:')
    if(mode == 'max'):
        data = starFunctions.maxMeanByInterval(start, end, MONTHLY)
        print(f"Ano do máximo: {data['year']}")
        print(f"Mês de máximo: {data['month']}")
        print(f"Total de manchas: {data['max']}")
        input('Aperta qualquer tecla para continuar')
    else:
        data = starFunctions.minMeanByInterval(start, end, MONTHLY)
        print(f"Ano do mínimo: {data['year']}")
        print(f"Mês de mínimo: {data['month']}")
        print(f"mínimo de manchas: {data['min']}")
        input('Aperte qualquer tecla para continuar')

#-----------------------------------------------------------------

#-----------------------------------------------------------------
def menuMaxMin(mode):

    os.system(CLEAR_COMMAND)

    start = int(input('Digite o ano de início: '))
    end = int(input('digite o ano final da consulta: '))
    startMonth = int(input('Digite o mês de início: '))
    endMonth = int(input('digite o mês final da consulta: '))

    if(start < 1818 or end > 2022 or startMonth < 1 or startMonth > 12 or endMonth < 1 or endMonth > 12 or end > 1818):
        while(start < 1818 or end > 2022):
            os.system(CLEAR_COMMAND)
            print('Os anos selecionados estão fora do range de anos')
            print('Digite anos entre 1818 e 2022')
            start = int(input('Digite o ano de início: '))
            end = int(input('digite o ano final da consulta: '))
            startMonth = int(input('Digite o mês de início: '))
            endMonth = int(input('digite o mês final da consulta: '))
            
    data = starFunctions.maxMinByInterval(start, end, startMonth, endMonth, DAILY)

    os.system(CLEAR_COMMAND)
    print('No intervalo dado, os resultados foram os seguintes:')
    if(mode == 'max'):
        print(f"Ano do máximo: {data['maximum']['year']}")
        print(f"Mês de máximo: {data['maximum']['month']}")
        print(f"Dia de máximo: {data['maximum']['day']}")
        print(f"Total de manchas: {data['maximum']['max']}")
        input('Aperte qualquer tecla para continuar')
    else:
        print(f"Ano do mínimo: {data['minimum']['year']}")
        print(f"Mês de mínimo: {data['minimum']['month']}")
        print(f"Dia de mínimo: {data['minimum']['day']}")
        print(f"mínimo de manchas: {data['minimum']['minimum']}")
        input('Aperte qualquer tecla para continuar')
        os.system(CLEAR_COMMAND)
        



#-----------------------------------------------------------------

#-----------------------------------------------------------------
def menuConsulta():
    option = 9999
    os.system(CLEAR_COMMAND)
    while(option != 6):
        os.system(CLEAR_COMMAND)
        print('DIGITE A OPÇÃO DE CONSULTA')
        print('--------------------------------------')
        print('1 - Máximo de manchas solares diárias em determinado período de anos')
        print('2 - Mínimo de manchas solares diárias em determinado período de anos')
        print('3 - Maior média mensal em um período da anos')
        print('4 - Menor média mensal em um período de anos')
        print('5 - Voltar para menu principal')
        print('6 - Sair')
        option = int(input('Digite a opção: '))

        

        if(option == 1):
            menuMaxMin('max')
            os.system(CLEAR_COMMAND)
        elif(option == 2):
            menuMaxMin('min')
            os.system(CLEAR_COMMAND)
        elif(option == 3):
            maxMinMean('max')
            os.system(CLEAR_COMMAND)
        elif(option == 4):
            maxMinMean('min')
            os.system(CLEAR_COMMAND)
        elif(option == 5):
            menuPrincipal()
            os.system(CLEAR_COMMAND)
        elif(option == 6):
            sys.exit()
        else:
            print('Opção não existente')
            input('Aperte qualquer tecla para continuar')
            os.system(CLEAR_COMMAND)
        os.system(CLEAR_COMMAND)
#-----------------------------------------------------------------

#------------------------------------------------------------------
#FUNÇÕES NECESSÁRIAS PARA GERAR GRÁFICO

def plotGraphMenu():
    os.system(CLEAR_COMMAND)
    start = int(input('Digite o ano de início do gráfico: '))
    end = int(input('Digite o ano final do gráfico: '))

    if(start > end or start < 1818 or end > 2022):
        print('Anos fora do limite, digite anos entre 1818 e 2022.')
        while(start > end or start < 1818 or end > 2022):
                os.system(CLEAR_COMMAND)
                print('Anos fora do limite, digite anos entre 1818 e 2022.')
                start = int(input('Digite o ano de início do gráfico: '))
                end = int(input('Digite o ano final do gráfico: '))
    
    data = starFunctions.dataForGraph(DAILY, MONTHLY, start, end)
    title = starFunctions.createGraph(data)

    print(f'O gráfico foi salvo com o título {title}')
    input('Aperte Enter para continuar')

#------------------------------------------------------------------

#-----------------------------------------------------------------
def menuPrincipal():
    option = 0
    os.system(CLEAR_COMMAND)
    while(option != 3):
        os.system(CLEAR_COMMAND)
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
        if(option == 1):
            menuConsulta()
        elif(option == 2):
            plotGraphMenu()
        elif(option == 3):
            sys.exit()
        else:
            print('Opção não existente')
            input('Aperte qualquer tecla para continuar')
            os.system(CLEAR_COMMAND)

#-----------------------------------------------------------------

