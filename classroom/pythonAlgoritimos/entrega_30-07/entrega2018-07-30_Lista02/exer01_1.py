'''Considere um arquivo de entrada no formato CSV (comma separated values)
com informações relativas a acidentes na aviação civil brasileira nos últimos 10
anos (arquivo anv.csv)
• As informações estão separadas pelo caracter separador ~ e entre “” (aspas)

Crie uma função que efetue a leitura do arquivo e processe seus dados identificando o total de ocorrencias no 
período avaliado e, baseado nessa informação criar um arquivo de saída em formato JSON (statistics.json) com as
seguintes as estatísticas (número de ocorrências e percentual do total) por fase de operação (coluna airplainOperationphase), 
como o exemplo a seguir:

[
 {
  "fase_operacao": "INDETERMINADA",
  "ocorrencias": 71,
  "percentual": "1,369%"
 },
 {
  "fase_operacao": "MANOBRA",
  "ocorrencias": 161,
  "percentual": "3,103%"
 },
...,
 {
  "fase_operacao": "APROXIMAÇÃO FINAL",
  "ocorrencias": 234,
  "percentual": "4,510%"
 }
]	
autor: Rafael Gimenes Leite <falecom@rafaelgimenes.net> 2018-07-22 
'''
from array import *
import json

def createJsonFile(jsonContent, totOccurrences):
    print('Total Occurrences', totOccurrences)
    
    listStatistics = []
    
    #JSON corpo da lista
    for item in jsonContent:
        listStatistics.append({
            'fase_operacao':item[0],
            'ocorrencias': item[1],
            "percentual": str(round((int(item[1])*100)/int(totOccurrences), 3)) +'%'
        })
    print(listStatistics)
    
    #abre o arquivo e dropa a lista no formato json
    with open('statistics.json', 'w') as outfile:
        json.dump(listStatistics, outfile,indent=4,)


def procTable(tableIN):
    airplaineOperationPhase = [] #crio array pra guardar todas das fases da operação
    for line in tableIN:
        celloperAtioNphase = line[20] #pegando cada fase de cada linha do arquivo
        
        # check pra ver se o valor da celula do arquivo ja foi pro array airplainOperationPhase
        x=[] 
        try:
            #https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement
            #print([x for x in airplaineOperationPhase if celloperAtioNphase in x][0])
            x = [x for x in airplaineOperationPhase if celloperAtioNphase in x][0] # procura o item, se nao explode index Out of bounds
        except IndexError:
            x = [] # ja esta vazio mas tem que fazer algo aqui excecao

        
        if len(x) == 0:
            # check se a fase operação nao foi,insert nele proxima posicao
            airplaineOperationPhase.insert(len(airplaineOperationPhase)+1 , [celloperAtioNphase, 0])
        else:
            #se foi localizado
            idxA = airplaineOperationPhase.index(x) #posição da fase operação no array
            updA = airplaineOperationPhase[idxA][1] #valor antigo do total da fase
            airplaineOperationPhase[idxA][1] = updA + 1  # mais 1 no total da fase

    return airplaineOperationPhase


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


table = readFile('anv.csv','~')
jsonBody = procTable(table)
createJsonFile(jsonBody, len(table))

'''
OUTPUT:
Total Occurrences 5188
[{'ocorrencias': 171, 'fase_operacao': 'UNKNOWN', 'percentual': '3.296%'}, 
{'ocorrencias': 393, 'fase_operacao': 'MANEUVERING', 'percentual': '7.575%'}, 
{'ocorrencias': 448, 'fase_operacao': 'APPROACH', 'percentual': '8.635%'}, 
{'ocorrencias': 1515, 'fase_operacao': 'LANDING', 'percentual': '29.202%'},
{'ocorrencias': 1241, 'fase_operacao': 'EN ROUTE', 'percentual': '23.921%'}, 
{'ocorrencias': 802, 'fase_operacao': 'TAKEOFF', 'percentual': '15.459%'}, 
{'ocorrencias': 438, 'fase_operacao': 'TAXI', 'percentual': '8.443%'}, 
{'ocorrencias': 160, 'fase_operacao': 'STANDING', 'percentual': '3.084%'}, 
{'ocorrencias': 5, 'fase_operacao': 'PUSHBACK/TOWING', 'percentual': '0.096%'},
{'ocorrencias': 1, 'fase_operacao': 'UNCONTROLLED DESCENT', 'percentual': '0.019%'}, 
{'ocorrencias': 0, 'fase_operacao': 'NOT APLICABLE', 'percentual': '0.0%'}, 
{'ocorrencias': 1, 'fase_operacao': 'EMERGENCY DESCENT', 'percentual': '0.019%'}, 
{'ocorrencias': 0, 'fase_operacao': '***', 'percentual': '0.0%'}]


'''