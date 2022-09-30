''' Autor Rafael Gimenes  Leite <rafaone@gmail.com>
    Data: 2018-06-23
'''

def fFor( numero):
    resul = numero
    for x in range(numero-1,0,-1):
        resul = resul * (x)
    return resul

print (fFor(6))

def fWhile(numero):
    resul = numero
    while numero > 1:
        numero = numero - 1
        resul = resul * (numero)
    return resul

print (fWhile(6))