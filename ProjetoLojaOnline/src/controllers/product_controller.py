from models.product import Product
import streamlit as st

#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4
class ProductController():
    def __init__(self) -> None:

        #Carrega dados do produto
        self.products = [
            Product(name="Fifa 22", price="250.00"),
            Product(name="Forza Horizon 5", price="200.00"),
            Product(name="Madden 22", price="250.00"),
            Product(name="The Last of Us 2", price="250.00"),
            Product(name="Shadow of the Tomb Raider", price="150.00"),
            Product(name="Red Dead Redemption 2", price="200.00")
        ]
    
    def check_product(self, product):
        return product in self.products

    def carrinho(self, name, price):
        product_teste = Product(name=name, price=price)
        for product in self.products:
            if product.name == product_teste.name and product.price == product_teste.price:
                return st.write(f'{name} - R$:{price}')
                
