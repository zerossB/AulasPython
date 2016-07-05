import os

def inserir():
    os.system("clear")
    nome = input("Digite um nome:")
    lista.append(nome)
    option[5]()

def alterar():
    os.system("clear")
    option[5]()

def deletar():
    os.system("clear")
    option[5]()

def listar():
    os.system("clear")
    option[5]()

def menu():
    os.system("clear")
    print("Escolha uma opção do menu:")
    print("    1- Inserir")
    print("    2- Alterar")
    print("    3- Deletar")
    print("    4- Listar")
    print("    0- Sair")
    user = input("Opção: ");
    option[user]()
