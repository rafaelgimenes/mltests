'''Exercicio 2
• Crie um programa que efetue a leitura do arquivo produzido no exercício 1
(levels.csv) e mostre na tela as seguintes informações estatísticas:
• Qtde total de acidentes
• Qtde total de acidentes agrupados por tipo de aeronave (type)
• Ano e fabricante da aeronave mais antiga (year_manufacturing, manufacturer)
• Qtde de assentos e tipo de motor da aeronave mais nova (seating,
engine_type)
• A quantidade de acidentes que ocorreram com aeronaves do tipo (type)
HELICÓPTERO, cuja fabricação se deu após o ano 1997
• A quantidade de acidentes que ocorreram com aeronaves do tipo (type) AVIÃO
fabricadas (manufacturer) pela CESSNA AIRCRAFT
autor: Rafael Gimenes Leite <falecom@rafaelgimenes.net> 2018-07-22 
'''
from array import *

def readFile(fileName,separator):
    f = open (fileName).readlines() #lendo o arquivo
    header = f.pop(0) #guardando o cabeçalho e removendo ele da lista
    lineArray = [] #Array pra guardar linha
    tableArray = [] #array pra guardar tabela toda
    for line in f:
        splitLine = line.split(separator) #
        for item in splitLine:
            item = item.replace("\"", "") # rgexp cut aspas sempre
            lineArray.append(item)
        tableArray.append(lineArray)
        lineArray=[] #zerando pro prox
    return tableArray



def procTable(tableIN):
    totacCdtairplaNe = 0
    totacCdthel = 0
    totacCdtgeneral = 0
    listOftpAero = []
    anoFabricante = []
    
    for line in tableIN:
        splitLine = line[0].split(',')
        #print(splitLine)
        #Qtde total de acidentes - Salvando dados
        totacCdtgeneral += 1
        
        #  Ano e fabricante da aeronave mais antiga (year_manufacturing, manufacturer), guardando todos os anos e aeronaves em uma nova array guardando também dados de, Qtde de assentos e tipo de motor da aeronave mais nova (seating,engine_type)
        anoFabricante.insert(len(anoFabricante), [splitLine[2], splitLine[5], splitLine[6], splitLine[3]])
        
        
        #A quantidade de acidentes que ocorreram com aeronaves do tipo (type) HELICÓPTERO, cuja fabricação se deu após o ano 1997
        if ((int(splitLine[5])>1997) and (splitLine[1]=='HELICÓPTERO')):
            totacCdthel +=1 
        
        #A quantidade de acidentes que ocorreram com aeronaves do tipo (type) AVIÃO fabricadas (manufacturer) pela CESSNA AIRCRAFT
        if ((splitLine[2]=='CESSNA AIRCRAFT') and (splitLine[1]=='AVIÃO')):
            totacCdtairplaNe +=1 
        
        
        #• Qtde total de acidentes agrupados por tipo de aeronave (type)
        tpAero = splitLine[1]
        x=[] 
        try:
            x = [x for x in listOftpAero if tpAero in x][0] #https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement
        except IndexError:
            x = []  # ja esta vazio mas tem que fazer algo aqui excecao

        if len(x) == 0:
            # Se a fase operação nao foi ele localizado inclui a fase operação no array
            listOftpAero.insert(len(listOftpAero)+1 , [tpAero, 1])
        else:
            #se foi localizado
            idxA = listOftpAero.index(x) #Acha a posição da fase operação no array
            updAFO = listOftpAero[idxA][1] #pega o valor antigo do total daquela fase de operaçao
            listOftpAero[idxA][1] = updAFO + 1  # soma mais 1 no total daquela fase de operação


    print()
    print()
    print('Qtde total de acidentes = ' + str(totacCdtgeneral))
    for item in listOftpAero:
        print( 'Qtde total de acidentes agrupados por tipo, aeronave = ' + str(item[0]) + ' total de acidentes = ' + str(item[1]))
    
    #ordenando a lista de anoFabricante e pegando o primeiro item que contem a aeronave mais antiga
    anoFabricanteOrdenado =sorted(anoFabricante, key=lambda anoFabricante: anoFabricante[1])
    print ('fabricante da aeronave mais antiga = ' + str(anoFabricanteOrdenado[0][0]) + ', ano = '+ str(anoFabricanteOrdenado[0][1]) )
   
     #ordenando a lista de anoFabricante em order reversa e pegando o primeiro item que contem a Qtde de assentos e tipo de motor da aeronave mais nova
    anoFabricanteOrdenado =sorted(anoFabricante, key=lambda anoFabricante: anoFabricante[1], reverse=True)
    print ('fabricante da aeronave com mais = ' + str(anoFabricanteOrdenado[0][0]) + ', ano = '+ str(anoFabricanteOrdenado[0][1]) +', Qtde de assentos = '+ str(anoFabricanteOrdenado[0][2]) + ' e tipo de motor da aeronave mais nova = ' + str(anoFabricanteOrdenado[0][3]) )
    print('Qtde de acidentes que ocorreram com aeronaves do tipo (type) HELICÓPTERO, cuja fabricação se deu após o ano 1997 = ' + str(totacCdthel))
    print('Qrde de acidentes que ocorreram com aeronaves do tipo (type) AVIÃO fabricadas (manufacturer) pela CESSNA AIRCRAFT = ' + str(totacCdtairplaNe))



tableArray = readFile('levels.csv','~')
procTable(tableArray)

'''
OUTPUT:
/home/rgimenes/PycharmProjects/facens/venv/bin/python /home/rgimenes/PycharmProjects/facens/entrega2018-07-30_Lista02/exe02.py
/home/rgimenes/PycharmProjects/facens/venv/bin/python /home/rgimenes/PycharmProjects/facens/entrega2018-07-30_Lista02/exer02.py


Qtde total de acidentes = 38
Qtde total de acidentes agrupados por tipo, aeronave = HELICÓPTERO total de acidentes = 15
Qtde total de acidentes agrupados por tipo, aeronave = AVIÃO total de acidentes = 17
Qtde total de acidentes agrupados por tipo, aeronave = ULTRALEVE total de acidentes = 6
fabricante da aeronave mais antiga = CESSNA AIRCRAFT, ano = 1946
fabricante da aeronave com mais = ROBSON DIAS LIMA, ano = 2011, Qtde de assentos = 2 e tipo de motor da aeronave mais nova = PISTÃO
Qtde de acidentes que ocorreram com aeronaves do tipo (type) HELICÓPTERO, cuja fabricação se deu após o ano 1997 = 6
Qrde de acidentes que ocorreram com aeronaves do tipo (type) AVIÃO fabricadas (manufacturer) pela CESSNA AIRCRAFT = 6

Process finished with exit code 0
'''