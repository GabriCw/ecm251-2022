################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################

class Cart():

    def __init__(self):
        self._products=[]

    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products
        
    def __str__(self):
        return self._products