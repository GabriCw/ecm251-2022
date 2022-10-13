from models.product import Product
import streamlit as st

#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4
class ProductController():
    def __init__(self) -> None:

        #Carrega dados do produto
        self.products = [
            Product(name="Fifa 22", description="EA Sports", price=249.99),
            Product(name="Forza Horizon 5", description="Playground Games", price=199.99),
            Product(name="Madden 22", description="EA Sports", price=249.99),
            Product(name="The Last of Us 2", description="Sony Interactive", price=249.99),
            Product(name="Shadow of the Tomb Raider", description="Crystal Dynamics", price=149.99),
            Product(name="Red Dead Redemption II", description="Rockstar", price=199.99)
        ]
    
    def check_product(self, product):
        return product in self.products
    
    def get_nome(self, name):
        for product in self.products:
            if product.name == name:
                return f'{product.name} \n{product.description}' 
    
    def get_price(self, name):
        for product in self.products:
            if product.name == name:
                return product.price

    def carrinho(self, name):
        for product in self.products:
            if product.name == name:
                return st.write(f'{product.name} - R$: {product.price}')
                
