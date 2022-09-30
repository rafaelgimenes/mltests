'''
Exercicio Final
@author Rafael Gimenes Leite <falecom@rafaelgimenes.net>

'''
import csv
from datetime import datetime
from itertools import groupby
from operator import attrgetter
from operator import itemgetter
#lista publica pra aproveitar nas 2 partes do exercicio.
elections = []

class Election2016(object):
    def __init__(self, table):
        self.cod_municipio_tse = table['cod_municipio_tse']
        self.uf = table['uf']
        self.nome_municipio = table['nome_municipio']
        self.total_eleitores = table['total_eleitores']
        self.f_16 = table['f_16']
        self.f_17 = table['f_17']
        self.f_18_20 = table['f_18_20']
        self.f_21_24 = table['f_21_24']
        self.f_25_34 = table['f_25_34']
        self.f_35_44 = table['f_35_44']
        self.f_45_59 = table['f_45_59']
        self.f_60_69 = table['f_60_69']
        self.f_70_79 = table['f_70_79']
        self.f_sup_79 = table['f_sup_79']
        self.gen_feminino = int(table['gen_feminino'])
        self.gen_masculino = int(table['gen_masculino'])
        self.gen_nao_informado = int(table['gen_nao_informado'])

    def __str__(self):
        return str(vars(self))


def save_csv(file, header, content):
    with open(file, 'w', newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(map(vars, content)))
    f.close()

def save_txt(file, content):
    with open(file, 'w') as f:
        for line in content:
            f.write(str(line) + '\n')
    f.close()




#parte 1
with open('BR_eleitorado_2016_municipio.csv', 'r', encoding='utf-8') as f:
    # read data from Election into list of Election data
    reader = csv.DictReader(f, delimiter=';')
    elections = [Election2016(e) for e in reader]

    # filter / sorted uf
    #sorted_by_uf = sorted(list(filter(lambda e: ('' != e.uf), elections)), key=attrgetter('uf'))
    sorted_by_uf = sorted(elections, key=attrgetter('uf'))
    # filter  sorted sorted_by_codMun
    #sorted_by_codMun = sorted(list(filter(lambda e: (e.cod_municipio_tse>0), sorted_by_uf)), key=attrgetter('cod_municipio_tse'))
    sorted_by_codMun = sorted(sorted_by_uf, key=attrgetter('cod_municipio_tse'))


    # save CVS file
    header = ['cod_municipio_tse','uf','nome_municipio','total_eleitores','f_16','f_17','f_18_20','f_21_24','f_25_34','f_35_44','f_45_59','f_60_69','f_70_79','f_sup_79','gen_feminino','gen_masculino','gen_nao_informado']
    #save_csv('pleito_2016_classificado.csv', header, sorted_by_codMun)


    f.close()

#parte 2
def group_female_by_uf(tableIN):

    #Jeito Legivel list comprehension tupla uf, gem feminino já ordenado por UF
    listUFGenFem = [ (e.uf,e.gen_feminino) for e in sorted(tableIN, key=attrgetter('uf'))]
    listUFGenFemTotal = []
    soma=0 #variavel soma
    for key, items in groupby(listUFGenFem, itemgetter(0)): #varre uf
        soma=0 #zera a soma qdo novo UF
        for subitem in items:
            soma=soma+int(subitem[1])
        #add tupla
        listUFGenFemTotal.append((key,soma))

    print(listUFGenFemTotal)


    #jeito vomitado
    resul =  [(key, sum(i[1] for i in items)) for key,items in groupby(((e.uf,e.gen_feminino) for e in sorted(tableIN, key=attrgetter('uf'))),itemgetter(0))]

    print(resul)


group_female_by_uf(elections)


#parte 3































