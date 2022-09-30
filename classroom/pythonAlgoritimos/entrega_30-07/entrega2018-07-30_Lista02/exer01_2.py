'''2. Crie um arquivo de saida
(formato CSV) com nome
levels.csv contendo as
seguintes informações:
• operation -> aeronave_operador_categoria
• type -> aeronave_tipo_veiculo
• manufacturer -> aeronave_fabricante
• engine_type aeronave_motor_tipo
• engines -> aeronave_motor_quantidade
• year_manufacturing -> aeronave_ano_fabricacao
• seating -> aeronave_assentos
• fatalities -> total_fatalidades
Considerando apenas acidentes cujo nível de dano da aeronave tenha sido
LEVE ou NENHUM (coluna aeronave_nivel_dano) E que o número de
fatalidades (total_fatalidades) tenha sido superior à 0 (zero)
OBS: Efetuar apenas uma leitura do arquivo de entrada
autor: Rafael Gimenes Leite <falecom@rafaelgimenes.net> 2018-07-22 
'''

def writeCSVFile(line):
    f= open("levels.csv","a+")
    f.write(line + '\n')
    f.close


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


def createCSVFile (tableIN):
    for line in tableIN:
        try:
            if (int(line[23])>0 and (line[22]=='NENHUM' or line[22]=='LEVE')):
                lineA = line[2] +','+line[3]+','+line[4]+','+line[7]+','+line[8]+','+line[12]+','+line[11]+','+line[23]
                writeCSVFile(lineA)
        except ValueError:
            print('Erro coversao Int')

table = readFile('anv.csv','~')
createCSVFile(table)


'''
OUTPUT:
Sem output apenas level.csv
'''