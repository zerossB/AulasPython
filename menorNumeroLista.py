def menorLista(numeros):
	minimo = numeros[0]
	for numero in numeros[1:]:
		if numero < minimo:
			minimo = numero
	return minimo

print(menorLista([3,5,2,0,1,2,-1,10]))
	
