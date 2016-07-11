texto = "{} Bem vindo ao {}"
print(texto.format('Haynes', 'zeus'))

texto1 = "{nome} Bem vindo ao {prog}"
print(texto1.format(prog='Haynes', nome='zeus'))

form = " {0:<10} | {1:<10} | {2:<10} "
print(form.format("aisjk", "oau2", "oak0101-"))

form = " {0:^10} | {1:^10} | {2:^10} "
print(form.format("aisjk", "oau2", "oak0101-"))

form = " {0:=^10} | {1:_<10} | {2:->10} "
print(form.format("aisjk", "oau2", "oak-"))

print("\n\n\n")
formato_tabela = " {0:^6} | {1:^9} | {2:^10} "
formato_body = " {0:^6} | {1:^9} | {2:^10.2f} "
produtos = [
    (200, 'Amarelo', 18.50),
    (312, 'Vermelho', 48.75),
    (20, 'Branco', 78.15)
]
print(formato_tabela.format('Qtd.', 'Cor', 'Valor R$'))
for qtd, cor, valor in produtos:
    print(formato_body.format(qtd, cor, valor))

print('\n\n\n')
import math

pi = math.pi
print(format(pi, '3.20'))
print(format('Python', '.<20'))
print(format('Python', '.>20'))
print(format('Python', '.^20'))


print('\n\n\n')

lista1 = [1, 1, 1, 2, 2, 3, 3, 3, 3]
print(list(set(lista1)))

A = {5, 4, 3, 3, 2, 10, 20}
print(len(A))
print(sum(A))
print(max(A))
print(min(A))
print(A)
for x in A:
    print(x)

print("")
B = {num for num in range(30) if num % 3 != 0}
for x in B:
    print(x)

print(5 in B)
print(6 in A)

print("\n\n\n")
import timeit
tempo = timeit.timeit('[math.exp(x) for x in range(10)]', setup="import math")
print(tempo)
