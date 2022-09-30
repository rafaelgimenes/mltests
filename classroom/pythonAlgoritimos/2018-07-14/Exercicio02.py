herois_masc = []
herois_fem = []
herois_sem = []
herois_mcdc = []
viloes_azul=[]
def processa(caminho):
    f = open(caminho, 'r')
    csv = f.readlines()
    f.close()
    linha=[]
    for i in range(1,len(csv),1):
        linha = csv[i].split(',')
        if linha[2]=='Male':
            l = [linha[0],linha[1]]
            herois_masc.append(l)
        if linha[2]=='Female':
            l = [linha[0], linha[1]]
            herois_fem.append(l)
        if linha[2] == '-':
            l = [linha[0], linha[1]]
            herois_sem.append(l)
        if linha[7]=='DC Comics' or linha[7]=='Marvel Comics':
            l=[linha[1]]
            herois_mcdc.append(l)
        if linha[8]=='blue' and linha[9]=='bad':
            l=[linha[1]]
            viloes_azul.append(l)
    criaArquivo('heroisMac.csv', herois_masc, 'id,nome', ',', '\n')
    criaArquivo('heroisFem.csv', herois_fem, 'id,nome', ',', '\n')
    criaArquivo('heroisSem.csv', herois_sem, 'id,nome', ',', '\n')
    criaArquivo('viloesBlue.txt', viloes_azul, '', '', '#')
    criaArquivo('heroiDC.csv', herois_mcdc, '', ',', '\n')

def criaArquivo(nome,lista,header,separador,quebra):
    f = open(nome, 'w')
    if(header != ''):
        f.write(header+quebra)
    k=0
    for item in lista:
        i = 0
        for ele in item:
            f.write(ele)
            if(i<len(item)-1):
                f.write(separador)
            i = i + 1
        if ( k < len(lista)-1):
            f.write(quebra)
        k=k+1
    f.close()
processa('heroes_information.csv')

