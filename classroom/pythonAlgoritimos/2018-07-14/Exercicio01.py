''' Autor Rafael Gimenes  Leite <rafaone@gmail.com>
    Data: 2018-07-14
'''
from datetime import datetime

def exer(caminho):
    f = open(caminho, 'r')
    linhas = f.readlines()
    f.close()
    listaPrincipal=[]
    listaFiltrada=[]
    listaFiltrada2=[]
    listaNomes = []

    for i in range(0,len(linhas),1):
        nome = linhas[i][0:6].strip()
        tam = linhas[i][6:6+6]
        data = linhas[i][12:12+12].rstrip()
        listaTemp  = [nome,tam,data]
        listaPrincipal.append(listaTemp)

    for a in range (0,len(listaPrincipal),1):
        s = listaPrincipal[a][1]
        letra = s[-1:].strip().upper()
        if letra=='K':
            num = int(float(s[:-1]) * 1024)
        elif letra == 'M':
            num = int(float(s[:-1]) * 1024*1024)
        else:
            num = int(s[:-1])

        if num < (2*(2**20)):
            listaFiltrada.append(listaPrincipal[a])

    for x in range (0,len(listaFiltrada),1):
        data = listaFiltrada[x][2].lstrip()
        o = datetime.strptime(data,'%d %b %Y')
        c = datetime.strptime('28 Feb 2000','%d %b %Y')
        if(o<c):
            listaFiltrada2.append(listaFiltrada[x])
            listaNomes.append(listaFiltrada[x][0])

    cnt = 0;
    resul = 0;
    for f in range(0,len(listaFiltrada2),1):
        cnt = listaNomes.count(listaFiltrada2[f][0])
        if cnt > 1:
            resul=resul+1
    return resul

print(exer('files.txt'))
