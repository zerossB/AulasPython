import os
import sys

from pathlib import Path

def tableList(lista, args):
    thead_nome  = "Nome".ljust(30, " ")
    thead_ext   = "Ext".center(10, " ")
    thead_perm  = "Perm".center(10, " ")

    title       = " Listando Arquivos do diretorio ".center(80, "#")
    if args[1] == "./":
        diret       = os.path.dirname(os.getcwd()).center(80, " ")
    else:
        diret       = os.path.dirname(str(args[1])).center(80, " ")

    arq_name    = ""
    arq_ext     = ""
    arq_perm    = ""

    print(title)
    print(diret)
    print("")
    print(thead_nome, thead_ext, thead_perm)

    listDir = []

    for arq in lista:
        if os.path.isfile(os.path.abspath(arq)) == True:
            try:
                ext = str(arq).split(".")
                listDir.append([arq, ext[1], ""])
            except IndexError:
                listDir.append([arq, "", ""])

        #elif os.path.isdir(os.path.abspath(arq)) == True:
        else:
            listDir.append([arq, "dir", ""])

    for arq in listDir:
        arq_name    = arq[0]
        arq_ext     = arq[1]

        print(arq_name.ljust(30, " "), arq_ext.ljust(10, " "))

    print("")

def main(args):
    #print([arq for arq in os.listdir(args[1])])
    lista = [arq for arq in os.listdir(args[1])]
    lista.sort()
    tableList(lista, args)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        main(sys.argv)
    else:
        print("Desculpe há argumentos de mais")
        sys.exit(0)
