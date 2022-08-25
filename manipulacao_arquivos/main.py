#código para manipulação de um arquivo

from traceback import print_stack


try:
    arquivo = open("data/sistemas.txt", "a")
    continuar = True

    while continuar:
        os_name = input("Diga um OS (vazio para sair):")
        if not os_name:
            continuar = False
            continue  #força parar o laço e testar de novo a condição inicial
        arquivo.write(os_name +"\n")
    arquivo.close()
except FileNotFoundError:
    print("Caminho não existe, favor verificar")
except Exception:
    print("Algo não esperado ocorreu:")
    print_stack()
finally:
    print("Chegamos no final pessoal")