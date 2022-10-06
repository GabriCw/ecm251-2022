import re


#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f'Product(name:{self.name}, price:{self.price})'