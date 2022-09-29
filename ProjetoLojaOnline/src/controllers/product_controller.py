from models.product import Product

class ProductController():
    def __init__(self) -> None:

        #Carrega dados do produto
        self.products = [
            Product(name="Fifa 22", price="250.00"),
            Product(name="The Last of Us 2", price="250.00")
        ]
    
    def check_product(self, product):
        return product in self.products