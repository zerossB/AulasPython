clear
"""
    TESTE DE VALIDAÇÃO DE CNPJ COM PYTHON

    Autor  : Haynesss
    Data   : 04/07/2016
    License: GPL v3

"""
import os

#       5  0  3  7  7  1  5  8  0  0  0  1  0  6
dig1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
dig2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

soma = 0
digRes1 = 0
digRes2 = 0

os.system("clear")
cpf = input("Digite um CNPJ (Somente Numeros)")
print("\n")

listCNPJ = list(cpf)

"""
    Digito 1
"""

soma = 0

for a in range(0, 12):
    soma = soma + (int(dig1[a]) * int(listCNPJ[a]))
    print(soma)
