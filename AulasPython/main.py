import os

lista = []
user = 5;

def menu():
    os.system("clear")
    print("Escolha uma opção do menu:")
    print("    1- Inserir")
    print("    2- Alterar")
    print("    3- Deletar")
    print("    4- Listar")
    print("    0- Sair")
    user = int(input("Opção: "))
    execute_cmd(user)

def inserir():
    os.system("clear")
    nome = input("Digite um nome:")
    lista.append(nome)
    menu()

def alterar():
    os.system("clear")
    menu()

def deletar():
    os.system("clear")
    menu()

def listar():
    os.system("clear")
    for palavra in range(0, len(palavra)):
        print(palavra, lista[palavra])

def execute_cmd(num):
    if num == 0:
        os.system("clear");
        os.system("exit");
    elif num == 1:
        inserir()
    elif num == 2:
        alterar()
    elif num == 3:
        deletar()
    elif num == 4:
        listar()
    else:
        print("Selecione uma opção válida!")
        menu()

def main():
    menu()

#if __name__ == "__main__":
main()
