class Arvore:
    def __init__(self, nome):
        self.nome = nome
    def ola(self):
        return f'Ola eu sou {self.nome}'

class Alface:
    def __init__(self, nome):
        self.nome = nome 
    def ola(self):
        return f'Fala ae, eu sou {self.nome}'

#verifica se o arquivo do módulo é o principal na execução
if __name__ == "__main__":
    print('ola')