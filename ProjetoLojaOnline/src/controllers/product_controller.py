from models.product import Product

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