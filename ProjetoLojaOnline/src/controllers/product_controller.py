from models.product import Product
import streamlit as st

################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################
class ProductController():
    def __init__(self) -> None:

        ##########################
        #Carrega dados do produto#
        ##########################
        
        self.products = [
            Product(name="Booster Espada e Escudo", description="Contém 6 cards", price=11.99),
            Product(name="Booster XY", description="Contém 6 cards", price=84.99),
            Product(name="Booster Origem Perdida", description="(JAP) Contém 5 cards", price=25.99),
            Product(name="Triple Pack Pokemon Go", description="Contém 3 boosters", price=54.99),
            Product(name="Quadri Pack Golpe Fusão", description="Contém 3 boosters", price=89.99),
            Product(name="Booster Black & White", description="(EUA) Contém 10 cards", price=99.99),
            Product(name="Fichário Azul", description="20 folhas com 9 bolsos", price=129.99),
            Product(name="Sleeve Básica", description="100 sleeves de proteção", price=49.99),
            Product(name="Sleeve Charizard", description="65 sleeves de proteção", price=49.99),
            Product(name="Giratina V-ASTRO Gold", description="Coleção Origem Perdida", price=399.99),
            Product(name="Samurot V-ASTRO Rainbow", description="Coleção Estrelas Radiantes", price=199.99),
            Product(name="Mewtwo V", description="Coleção Pokemon Go", price=49.99),
            Product(name="Pikachu", description="Coleção Sol e Lua", price=7.99),
            Product(name="Gengar Full Art", description="Coleção Origem Perdida", price=39.99),
            Product(name="Charizard", description="Coleção Lendária", price=19999.99)
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
                
