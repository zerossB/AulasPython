def soma(num):
	soma = 0
	for x in num:
		soma = soma + x
	return soma

soma = soma([1, 2, 3, 4, 5, 6])
print(soma)

#assert soma(range(1, 7)) == 21
