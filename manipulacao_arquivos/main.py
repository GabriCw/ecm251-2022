#código para manipulação de um arquivo

arquivo = open("data/sistemas.txt", "a")
continuar = True

while continuar:
    os_name = input("Diga um OS (vazio para sair):")
    if not os_name:
        continuar = False
        continue  #força parar o laço e testar de novo a condição inicial
    arquivo.write(os_name +"\n")
arquivo.close()