# author Rafael Gimenes Leite
def chkPrimo(nEntrada):
    if nEntrada <= 55000000 and nEntrada >0:
        if nEntrada < 2:
            return False
        for i in range(2,nEntrada):
            if not nEntrada%i:
                return False
        return True  
    else:
        return "fora do range"

print(chkPrimo(11))