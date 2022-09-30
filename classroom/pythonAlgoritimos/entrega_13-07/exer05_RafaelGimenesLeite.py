# author Rafael Gimenes Leite, RA 101364
def somarListas(lista1,lista2):
	if len(lista1) == 0 and len(lista2) == 0:
		return -1
	lista3 = []
	diffe = len(lista1) - len(lista2)
	if diffe < 0:
		for x in range(len(lista1),len(lista2),1):
			lista1.extend([1])
	elif diffe > 0:
		for x in range(len(lista2),len(lista1),1):
			lista2.extend([1])
	for i in range(0,len(lista1),1):
		lista3.append(lista1[i]+lista2[i])	
	return (lista3)
print(somarListas([1],[88,99,5]))
