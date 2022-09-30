''' Autor Rafael Gimenes  Leite <rafaone@gmail.com>
    Data: 2018-06-23
'''

def soma(a,b):
    s=0
    if a<b:
        ini = a;
        fim = b;
    else:
        ini=b;
        fim=a;

    for x in range(ini , fim+1,1 ):
                s += x;
    return s

print soma(5,7)
