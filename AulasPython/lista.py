nomes = []

def main():

    for nm in range(0, 10):
        nomes.append("Nome %d" % (i))

    print(" Relatório do Haynes ".center(80, "-"));
    print(" Empresa: Cerâmica Stefani S/A ".ljust(30, " "))
    print(" Tabela de Nomes ".center(80, "_"))
    for i in range(0, 10):
        print("| ID: %d".ljust(11, " ") % (i), " | Nome: %d".ljust(58, " ") % (nomes[i]), " |")

main();
