################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################

import streamlit as st
import time
from models.product import Product
from dao.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self._products = ProductDAO.get_instance().get_all()

    def get_product(self,index):
        return self._products[index]
    
    def get_products(self):
        return self._products

    def sign_product(self, name, price, url, amount):
        product = Product(name, price, url, amount)

        teste = ProductDAO.get_instance().inserir_product(product)
        if teste == False:
            st.session_state["carrinho"] = "Falha ao Cadastrar"
            print(teste)
        else:
            st.session_state["carrinho"] = "Produto Cadastrado Com Sucesso"
            st.session_state["Login"] = "negado"
            time.sleep(0.2)
            st.session_state["Login"] = "aprovado"
    
    def update_product(self, name, amount):
        teste2 = ProductDAO.get_instance().atualizar_product(name, amount)
        if teste2 == False:
            st.session_state["carrinho"] = "Falha ao Editar"
            print(teste2)
        else:
            st.session_state["carrinho"] = "Produto Editado Com Sucesso"
            st.session_state["Login"] = "negado"
            time.sleep(0.2)
            st.session_state["Login"] = "aprovado"