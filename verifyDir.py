import os
import sys

def verify(ext, diret):
	lista = [arq for arq in os.listdir(diret) if arq.endswith(ext)]
	if lista == []:
		return "Desculpe, não existe arquivos com "+ext+" no diretório "+diret
	else:
		return lista


if len(sys.argv) < 3:
	print("Há argumentos de mais")
	print("Funciono da seguinte forma:")
	print("    verifyDir.py <extenção> <diretorio>")
	sys.exit(0)
else:
	print(verify(sys.argv[1], sys.argv[2]))

