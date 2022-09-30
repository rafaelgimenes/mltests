lista_resul = []
def processa(caminho):
    f = open(caminho, 'r')
    csv = f.readlines()
    f.close()
    linha=[]
    for i in range(1,len(csv),1):
        linha = csv[i].split(',')
        
    criaArquivo('resul.txt', lista_resul, '', '', '\n')

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

