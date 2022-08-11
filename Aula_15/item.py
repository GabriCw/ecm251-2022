class Item():
    #Método construtor
    def __init__(self, valor, descricao, nome):
        self._valor = valor 
        self._descricao = descricao 
        self._nome = nome 
    
    def get_valor(self):
        return self._valor 
    def get_descricao(self):
        return self._descricao
    def get_nome(self):
        return self._nome
    
    def __str__(self) -> str:
        return self._nome + " - R$" + str(self._valor)
    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o, Item)):
            return self._nome == __o.get_nome()
        return False