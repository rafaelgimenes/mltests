from builtins import filter


def readFile(fileName,separator):
    f = open (fileName).readlines() #lendo o arquivo
    header = f.pop(0) #guardando o cabeçalho e removendo ele da lista
    lineArray = [] #Array pra guardar linha
    tableArray = [] #array pra guardar tabela toda
    for line in f:
        splitLine = line.split(separator) #
        c = Customer(splitLine[0],splitLine[1],splitLine[2],splitLine[3],splitLine[4],splitLine[5].replace('\n',''))
        tableArray.append(c)
    return tableArray

def writeCSVFile(line,nome):
    f= open(nome+".csv","a+")
    f.write(line + '\n')
    f.close

def writeTxtFile(line,nome):
    f= open(nome+".txt","a+")
    f.write(line + '\n')
    f.close


class Customer:
    def __init__(self,id,name,gender,birthday,email,active):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday=birthday
        self.email=email
        self.active=active

    def csv(self):
        return self.id + ';' + self.name + ';' +  self.gender + ';' + self.birthday + ';' + self.email + ';' + self.active+';'

    def txt(self):
        return self.id + ' ' + self.name + ' ' +  self.gender + ' ' + self.birthday + ' ' + self.email + ' ' + self.active+''

tab = readFile('customers.csv',';')
ordenadoID = sorted(tab, key=lambda x: x.id)
ordenadoNome = sorted(tab, key=lambda x: x.name)
filtroInActivo =  list(filter(lambda x: (x.active == 'False' and x.gender=='Male'), ordenadoNome))
filtroActivo =  list(filter(lambda x: x.active == 'True', ordenadoID))
#filtroActivo = [x for x in ordenadoID if x.active == 'True']


for x in filtroInActivo:
    writeTxtFile(x.txt(),'male_inactives')

for x in filtroActivo:
    writeCSVFile(x.csv(),'actives')


