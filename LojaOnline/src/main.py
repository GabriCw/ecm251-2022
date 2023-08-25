import random
import streamlit as st

from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.cart_controller import CartController

p_controller = ProductController()

st.set_page_config(page_title="Liga Pokemon", page_icon="㊗")

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

        st.title("Bem vindo!😁")
        st.markdown("Faça seu Login para desfrutar de nossos serviços!")
        st.divider()

        email = st.text_input(
            label="Email",
            placeholder= "Digite seu email"
        )

        password = st.text_input(
            label="Senha",
            placeholder= "Digite sua senha",
            type = "password"
        )
        
        col1, col2 = st.columns(2)

        with col1:
            st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),email,password))

        with col2:
            st.button(label = "Registrar-se", on_click = UserController.sign_up_screen)
    
    if st.session_state['Login'] == 'errado':
        st.warning("Email ou senha incorretos!")
        
    if st.session_state["Login"] == "registro":
        st.title("Cadastro")

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
            st.button(
                label= "Voltar", 
                on_click= UserController.login_screen
            )

        with col2:
            st.button(
                label= "Cadastrar-se", 
                on_click= UserController.sign_up, 
                args = (UserController(),name, email, password, cpf)
            )

    if st.session_state["Login"] == "aprovado":

        st.title("Bem vindo a Liga Pokemon!😁")

if "Login" in st.session_state:

    if st.session_state["Login"] == "aprovado" and st.session_state["Email"] == "couto@gmail.com":
        tab1, tab2, tab3, tab4 = st.tabs(["🈹 | Home", "🛒 | Carrinho", "➕ | Cadastrar Produtos", "➕ | Alterar Estoque"])

        with st.sidebar: 
            
            if st.session_state["Profile"] == "dados":
                st.markdown(f"Nome: {st.session_state['Usuario']}")
                st.markdown(f"Email: {st.session_state['Email']}")
                st.markdown(f"CPF: {st.session_state['Cpf']}")

                st.button(
                    label="Mudar informações de login", 
                    key= 7852084,
                    on_click= UserController.change_login
                )

                st.button(label= "Sair", on_click= UserController.logout)

            if st.session_state["Profile"] == "change":

                email = st.text_input(
                    label="Email",
                    key = 10000,
                    placeholder="Digite seu novo email"
                )

                password = st.text_input(
                    label="Senha",
                    type = "password",
                    key = 323,
                    placeholder="Digite sua nova senha"
                )

                col3, col4 = st.columns(2)

                with col3:
                    st.button(
                        label = "Voltar",
                        key = 99785, 
                        on_click = UserController.go_back
                    )
                
                with col4:
                    st.button(
                        label= "Alterar", 
                        key = 1234675, 
                        on_click= UserController.change_data, 
                        args = (UserController(), email, password)
                    )
                
        with tab1:

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}", width=200)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity1 = cont.number_input(
                        label = "", 
                        key = 100 * (i+1), 
                        format = "%i", 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity1 >= 0:
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 200 * (i+12), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity1)
                        
                        )
                    else:
                        cont.markdown("Produto indisponivel")

                with col2:

                    product = p_controller.get_product(index = i + 1)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}",width=200)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity2 = cont.number_input(
                        label = "",  
                        format = "%i", 
                        key = 300 * (i+83), 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity2 >= 0:    
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 400 * (i+99), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity2)
                        
                        )
                    else:
                        cont.warning("Produto indisponivel")

        with tab2:

            col1, col2, col3 = st.columns(3,gap="large")

            col1.title("Produto")
            col2.title("Preço")
            col3.title("Quantidade")
             
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_names[i]}")

            with col2:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"R${product_prices[i]:.2f}")

            with col3:
                
                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_qtt[i]}")

            valor_total = st.session_state["Cart"].get_total_price()
            
            st.title(f"Valor total: R${valor_total:.2f} ")
            st.button(
                label = "Finalizar Pedido", 
                key = 998, 
                on_click= st.session_state["Cart"].clear_cart
            )
        
        with tab3:

            st.title("Cadastrar Produtos")
            
            name1 = st.text_input(
                label= "Nome",
                key = 2222,
                placeholder="Digite o nome do produto"
            )

            price1 = st.number_input(
                label="Preço",
                min_value=0,
                key = 4444
            )

            url1 = st.text_input(
                label="URL Da Imagem",
                key = 55555,
                placeholder="Digite o url da imagem do produto"
            )

            amount1 = st.number_input(
                label = "Quantidade",
                min_value=0,
                step=1,
                key = 66666
            )

            st.button(
                label= "Cadastrar produto", 
                on_click= ProductController.sign_product, 
                args = (ProductController(), name1, price1, url1, amount1)
            
            )
            st.markdown(st.session_state["carrinho"])

        with tab4:

            st.title("Editar Produtos")

            name2 = st.text_input(
                label= "Nome",
                key = 194,
                placeholder="Digite o nome do produto"
            )

            amount2 = st.number_input(
                label = "Quantidade",
                min_value=0,
                step=1,
                key = 195
            )

            st.button(
                label= "Editar produto", 
                #on_click= ProductController.update_product, 
                #args = (ProductController(), amount2, name2)
            )

            st.markdown(st.session_state["carrinho"])
    elif st.session_state["Login"] == "aprovado" and st.session_state["Email"] != "couto@gmail.com":
        tab1, tab2 = st.tabs(["🈹 | Home", "🛒 | Carrinho"])
        with st.sidebar:
            if st.session_state["Profile"] == "dados":
                    st.markdown(f"Nome: {st.session_state['Usuario']}")
                    st.markdown(f"Email: {st.session_state['Email']}")
                    st.markdown(f"CPF: {st.session_state['Cpf']}")

                    st.button(
                        label="Mudar informações de login", 
                        key= 7852084,
                        on_click= UserController.change_login
                    )

                    st.button(label= "Sair", on_click= UserController.logout)

            if st.session_state["Profile"] == "change":

                email = st.text_input(
                    label="Email",
                    key = 10000,
                    placeholder="Digite seu novo email"
                )

                password = st.text_input(
                    label="Senha",
                    type = "password",
                    key = 323,
                    placeholder="Digite sua nova senha"
                )
                
                col3, col4 = st.columns(2)

                with col3:
                    st.button(
                        label = "Voltar",
                        key = 99785, 
                        on_click = UserController.go_back
                    )
                
                with col4:
                    st.button(
                        label= "Alterar", 
                        key = 1234675, 
                        on_click= UserController.change_data, 
                        args = (UserController(), email, password)
                    )

        with tab1:

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}", width=200)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity1 = cont.number_input(
                        label = "", 
                        key = 100 * (i+1), 
                        format = "%i", 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity1 >= 0:
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 200 * (i+12), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity1)
                        
                        )
                    else:
                        cont.markdown("Produto indisponivel")

                with col2:

                    product = p_controller.get_product(index = i + 1)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}",width=200)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity2 = cont.number_input(
                        label = "",  
                        format = "%i", 
                        key = 300 * (i+83), 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity2 >= 0:    
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 400 * (i+99), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity2)
                        
                        )
                    else:
                        cont.warning("Produto indisponivel")

        with tab2:

            col1, col2, col3 = st.columns(3,gap="large")

            col1.title("Produto")
            col2.title("Preço")
            col3.title("Quantidade")
             
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_names[i]}")

            with col2:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"R${product_prices[i]:.2f}")

            with col3:
                
                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_qtt[i]}")

            valor_total = st.session_state["Cart"].get_total_price()
            
            st.title(f"Valor total: R${valor_total:.2f} ")
            st.button(
                label = "Finalizar Pedido", 
                key = 998, 
                on_click= st.session_state["Cart"].clear_cart
            )