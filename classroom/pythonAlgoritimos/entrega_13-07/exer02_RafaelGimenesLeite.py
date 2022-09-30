# author Rafael Gimenes Leite
def chkChar(palavra, caracter):
    i = 0
    while i < len(palavra):
        if palavra[i] == caracter:
            return i
        i = i+1
    return -1

print(chkChar("code coffe out.","t"))

