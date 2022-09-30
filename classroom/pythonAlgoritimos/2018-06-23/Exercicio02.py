''' Autor Rafael Gimenes  Leite <rafaone@gmail.com>
    Data: 2018-06-23
'''
def ret2TuplasParImpar(listao):
    listao.sort()
    impar = []
    par = []
    for i in listao:
        if (i % 2 == 0):
            par.append(i)
        else:
            impar.append(i)
    return (par,impar)

print ret2TuplasParImpar([7,8,9,61,55,43,5,4,9,7,44,22,33,3])
