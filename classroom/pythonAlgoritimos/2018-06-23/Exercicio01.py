''' Autor Rafael Gimenes  Leite <rafaone@gmail.com>
    Data: 2018-06-23
'''
def qualMaior(a,b,c):
    if b >= a:
        a = b
    if c >= a:
        a = c
    return a
print qualMaior(-88,0,-99)
