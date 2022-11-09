################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################

import random
import streamlit as st

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
from src.controllers.cart_controller import CartController

p_controller = ProductController()

st.set_page_config(page_title="Liga Pokemon", page_icon="assets/ligapokemon.png")

with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

if "Login" not in st.session_state:
    st.session_state["Profile"] = "dados"
    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
    st.session_state["falta"] = ""
    st.session_state["Cart"] = CartController()
    st.session_state["carrinho"] = ""

with st.sidebar:

    
    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":
        st.text("")
        st.text("")

        st.title("Faça seu Login 😁!")

        st.markdown("***")

        email = st.text_input(
            label="Email",
            placeholder= "Digite seu email",
            value="couto@gmail.com"
        )

        password = st.text_input(
            label="Senha",
            placeholder= "Digite sua senha",
            type = "password",
            value="1234"
        )
        
        st.text("")
        
        col1, col2 = st.columns(2)
        with col1:
            st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),email,password))
        with col2:
            st.button(label = "Registrar-se", on_click = UserController.sign_up_screen)
    
    if st.session_state['Login'] == 'errado':

        st.markdown("***")
        st.markdown("# Email ou senha incorretos!")
        
    if st.session_state["Login"] == "registro":
        st.text("")
        st.text("")

        st.title("Cadastro")

        st.markdown("***")

        name = st.text_input(
            label="Nome",
            key = 1,
            placeholder= "Digite seu nome"
        )

        email = st.text_input(
            label="Email",
            key = 2,
            placeholder= "Digite seu email"
        )

        password = st.text_input(
            label="Senha",
            type = "password",
            key = 3,
            placeholder= "Digite sua senha"
        )

        cpf = st.text_input(
            label="CPF",
            key = 4,
            placeholder= "Digite seu cpf"
        )

        col1, col2 = st.columns(2)
        with col1:
            st.text("")
            st.button(label= "Voltar", on_click= UserController.login_screen)
        with col2:
            st.text("")
            st.button(label= "Cadastrar", on_click= UserController.sign_up, args = (UserController(),name, email, password, cpf))

    if st.session_state["Login"] == "aprovado":

        st.text("")

        st.title(f"Bem vindo, {st.session_state['Usuario']}")
        st.markdown("***")
        st.button(label= "Sair", on_click= UserController.logout)
        st.markdown("***")

if "Login" in st.session_state:

    if st.session_state["Login"] == "aprovado":
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🙍‍♂️ | Perfil", "🈹 | Home", "🛒 | Carrinho", "💬 | Cadastrar Produto", "➕ | Alterar Estoque"])

        with tab1: 

            st.title("Perfil")
            
            if st.session_state["Profile"] == "dados":
                st.markdown("***")
                st.markdown(f"### Nome: {st.session_state['Usuario']}")
                st.markdown("***")
                st.markdown(f"### Email: {st.session_state['Email']}")
                st.markdown("***")
                st.markdown(f"### CPF: {st.session_state['Cpf']}")
                st.markdown("***")
                st.button("Mudar informações de login", key = 7852084, on_click = UserController.change_login_data)

            if st.session_state["Profile"] == "change":
                email = st.text_input(
                    label="Novo Email",
                    key = 82700,
                )

                password = st.text_input(
                    label="Nova Senha",
                    type = "password",
                    key = 56240,
                )

                col3, col4 = st.columns(2)

                with col3:
                    st.button(label = "Voltar", key = 99785, on_click = UserController.go_back)
                
                with col4:
                    st.button(label= "Alterar", key = 1234675, on_click= UserController.change_data, args = (UserController(), email, password))
        with tab2:

            st.title("Home")
            
            st.markdown("***")

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    c = st.container()
                    c.markdown(f"## {product.get_name()}")
                    try:
                        c.image(f"{product.get_url()}", width=200)
                    except:
                        c.image("https://www.thesslstore.com/blog/wp-content/uploads/2018/10/bigstock-Error-Browser-Vector-Icon-Fil-242176321-e1540917868244-300x300.jpg")
                    c.markdown(f"## R${product.get_price():.2f}")
                    quantity1 = c.number_input(label = "", key = 100 * (i+1), format = "%i", step = 1,min_value = 1, max_value = product.get_amount())
                    if product.get_amount() > 0 and product.get_amount() - quantity1 >= 0:
                        c.button(label = f"Adicionar {product.get_name()}", key = 200 * (i+12), on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
                    else:
                        c.markdown("## Produto indisponivel")
                with col2:

                    product = p_controller.get_product(index = i + 1)
                    c = st.container()
                    c.markdown(f"## {product.get_name()}")
                    try:
                        c.image(f"{product.get_url()}",width=200)
                    except:
                        c.image("https://www.thesslstore.com/blog/wp-content/uploads/2018/10/bigstock-Error-Browser-Vector-Icon-Fil-242176321-e1540917868244-300x300.jpg")
                    c.markdown(f"## R${product.get_price():.2f}")
                    quantity2 = c.number_input(label = "",  format = "%i", key = 300 * (i+83), step = 1,min_value = 1, max_value = product.get_amount())
                    if product.get_amount() > 0 and product.get_amount() - quantity2 >= 0:    
                        c.button(label = f"Adicionar {product.get_name()}", key = 400 * (i+99), on_click= st.session_state["Cart"].add_product, args = (product, quantity2))
                    else:
                        c.markdown("## Produto indisponivel")

        with tab3:

            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3 = st.columns(3,gap="large")
            col1.markdown("### Produto")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
            

            
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")

            with col2:

                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### R${product_prices[i]:.2f}")

            with col3:
                
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")

            st.markdown("***")
            valor_total = st.session_state["Cart"].get_total_price()
            
            st.markdown(f"## Valor total: R${valor_total:.2f} ")
            st.button(label = "Finalizar Pedido", key = 998, on_click= st.session_state["Cart"].clear_cart)
        
        with tab4:

            st.text("")
            st.text("")

            st.title("Cadastrar Produtos")

            st.markdown("***")
            
            name1 = st.text_input(
                label= "Nome",
                key = 190
            )

            price1 = st.number_input(
                label="Preço",
                key = 191
            )

            url1 = st.text_input(
                label="URL Da Imagem",
                key = 192
            )

            amount1 = st.number_input(
                label = "Quantidade",
                key = 193
            )

            st.text("")
            st.button(label= "Cadastrar produto", on_click= ProductController.sign_product, args = (ProductController(), name1, price1, url1, amount1))
            
            st.markdown("### " + st.session_state["carrinho"])

        with tab5:
            st.text("")
            st.text("")

            st.title("Editar Produtos")

            st.markdown("***")

            name2 = st.text_input(
                label= "Name",
                    key = 194,
            )

            amount2 = st.number_input(
                label = "Quantidade",
                    key = 195,
            )
            st.text("")
            st.button(label= "Editar produto", on_click= ProductController.update_product, args = (ProductController(), name2, amount2))
            
            st.markdown("### " + st.session_state["carrinho"])