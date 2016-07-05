"""
    TESTE DE VALIDAÇÃO DE CPF COM PYTHON

    Autor  : Haynesss
    Data   : 04/07/2016
    License: GPL v3
    
"""
import os

#      [ 4,  4, 1, 0, 8, 8, 4, 1, 8, 2, 4]
dig1 = [10,  9, 8, 7, 6, 5, 4, 3, 2]
dig2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

soma = 0
digRes1 = 0
digRes2 = 0

os.system("clear")
cpf = input("Digite um CPF (Somente Numeros)")
print("\n")

listCPF = list(cpf)

"""
    Digito 1
"""
for a in range(0, 9):
    soma = soma + (int(dig1[a]) * int(listCPF[a]))

digRes1 = soma % 11

if digRes1 <= 2:
    digRes1 = 0
else:
    digRes1 = 11 - digRes1

"""
    Digito 2
"""
resto = 0
soma = 0

for b in range(0, 10):
    soma = soma + (int(dig2[b]) * int(listCPF[b]))

digRes2 = soma % 11

if digRes2 <= 2:
    digRes2 = 0
else:
    digRes2 = 11 - digRes2

if int(listCPF[9]) == int(digRes1) and int(listCPF[10]) == int(digRes2):
    print("CPF Válido")
else:
    print("CPF Inválido")

print("\n")
