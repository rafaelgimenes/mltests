#Exercicio 05

def somarListas(lista1,lista2):
    listaAuxPrincipal = []
    listaAuxSecundaria = []

    if len(lista1) != 0 or len(lista2) != 0:
        if len(lista1) > len(lista2):
            for n in range(0,len(lista2),1):
                listaAuxPrincipal.append(lista1[n] + lista2[n])
            for x in range(len(lista2),len(lista1),1):
                listaAuxSecundaria.append(lista1[x] + 1)

        else:
            for h in range(0, len(lista1), 1):
                listaAuxPrincipal.append(lista1[h] + lista2[h])
            for p in range(len(lista1), len(lista2), 1):
                listaAuxSecundaria.append(lista2[p] + 1)

        return (listaAuxPrincipal + listaAuxSecundaria)
    else:
        return -1

#Main()
print(somarListas([20,40,5,10],[13,2,7,5,10,20]))
