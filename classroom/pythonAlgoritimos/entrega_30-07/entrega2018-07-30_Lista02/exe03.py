'''Crie um programa que efetue a leitura do
arquivo (cota_parlamentar_sp.csv) e para
cada legenda (sgpartido) grave um
arquivo com o nome da legenda no
formato JSON (ex: DEM.json, PSDB.json)
• Em cada arquivo deverá conter as
seguintes informações conforme exemplo
ao lado:
• legenda (partido)
• nome (nome do parlamentar)
• total (total de despesas do parlamentar)

autor: Rafael Gimenes Leite <falecom@rafaelgimenes.net> 2018-07-22
'''

from array import *
import json

def createAppendJson(legend,listSum):
    #fazer o append no legend Json
    #importante a cada execução deletar os arquivos pre-existentes pois se nao ele vai abrir e dar append
    resul = []
    try:
        json_data = open(legend+'.json').read()
        resul = json.loads(json_data)
    except IOError:
        print('Arquivo Inexistente vamos abrir')

    # criando o conteudo para o arquivo JSON
    resul.append({
    'legenda': listSum[3],
    'nome': listSum[1],
    "total": listSum[2]
    })


    # Salvando estatisticas no arquivo JSON
    fileOut = legend+'.json'
    with open(fileOut, 'w') as outfile:
        json.dump(resul, outfile, indent=4, )

    print('Arquivo Processado: ' + fileOut)

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
    orderByFDP = sorted(tableIN, key=lambda x: x[1]) #ordena pelo deputado fica mais rapido do que por partido
    cuttedList=[] #nova lista capada idDeputado Legenda, nome valores
    listOfLegends = []  # lista somente dos partidos
    listOfFDP = []
    for item in orderByFDP:
        items = [item[5],item[1],item[6],item[10]]
        cuttedList.append(items)
        fDPx=[item[1],item[5]]
        if items[0] not in listOfLegends:
            listOfLegends.append(items[0])
        if fDPx not in listOfFDP:
            listOfFDP.append([item[1],item[5]])

    # soma os total dos FDP
    listOfSumFDP = []
    for itemA in listOfFDP:
        sumValue = 0
        legend=''
        name = ''
        for itemB in cuttedList:
            if itemA[1]==itemB[0]: #compara partido
                if (itemB[1]==itemA[0]): # comparada FDP
                    sumValue += int(itemB[3])
                    if (name == ''):
                        name=itemB[2]
                    if (legend==''):
                        legend=itemB[0]
        lTmp=[itemA[0], name, sumValue, legend]
        listOfSumFDP.append(lTmp)


    for itemC in listOfLegends:
        for itemD in listOfSumFDP:
            if itemC==itemD[3]:
                createAppendJson(itemC,itemD)


tableMain = readFile('cota_parlamentar_sp.csv',';')
procTable(tableMain)

'''
OUTPUT:
/home/rgimenes/PycharmProjects/facens/venv/bin/python /home/rgimenes/PycharmProjects/facens/entrega2018-07-30_Lista02/exe03.py
Arquivo Inexistente vamos abrir
Arquivo Processado: MDB.json
Arquivo Processado: MDB.json
Arquivo Processado: MDB.json
Arquivo Processado: MDB.json
Arquivo Processado: MDB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSOL.json
Arquivo Processado: PSOL.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Processado: PT.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSC.json
Arquivo Processado: PSC.json
Arquivo Processado: PSC.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PPS.json
Arquivo Processado: PPS.json
Arquivo Processado: PPS.json
Arquivo Processado: PPS.json
Arquivo Processado: PPS.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PROS.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Processado: PSDB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Processado: PR.json
Arquivo Inexistente vamos abrir
Arquivo Processado: SD.json
Arquivo Processado: SD.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PODE.json
Arquivo Processado: PODE.json
Arquivo Processado: PODE.json
Arquivo Processado: PODE.json
Arquivo Processado: PODE.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Processado: PSB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Processado: PP.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Processado: PRB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PV.json
Arquivo Processado: PV.json
Arquivo Processado: PV.json
Arquivo Processado: PV.json
Arquivo Processado: PV.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSD.json
Arquivo Processado: PSD.json
Arquivo Processado: PSD.json
Arquivo Processado: PSD.json
Arquivo Processado: PSD.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PDT.json
Arquivo Processado: PDT.json
Arquivo Processado: PDT.json
Arquivo Processado: PDT.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PMDB.json
Arquivo Processado: PMDB.json
Arquivo Processado: PMDB.json
Arquivo Processado: PMDB.json
Arquivo Processado: PMDB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Processado: DEM.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PTC.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PCdoB.json
Arquivo Processado: PCdoB.json
Arquivo Processado: PCdoB.json
Arquivo Processado: PCdoB.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PSL.json
Arquivo Processado: PSL.json
Arquivo Inexistente vamos abrir
Arquivo Processado: PTB.json
'''