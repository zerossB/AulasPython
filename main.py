#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

lista = list();
option = 5;

def menu():
    print("Digite uma opção:");
    print("    1- Adicionar");
    print("    2- Alterar");
    print("    3- Excluir");
    print("    4- Consultar");
    print("    0- Sair");
    option = input();
    
def inserir():
    print("Digite o Produto:");
    produto = input();
    lista.insert(len(lista), produto);
    os.system('cls' if os.name == 'nt' else 'clear');

def main():
    menu();    
    
    while(option != 0):
        if option == 1 :
            os.system('cls' if os.name == 'nt' else 'clear');
            insert();
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear');
            insert();
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear');
            insert();
        elif option == 4:
            os.system('cls' if os.name == 'nt' else 'clear');
            insert();

    exit();

if __name__ == "__main__":
    main();
