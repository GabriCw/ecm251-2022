import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController

#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

st.set_page_config(page_title="Loja Online", page_icon="🎮")
#Área de Login na sidebar
st.sidebar.title("Faça seu login para acessar os recursos da loja!😁")
st.sidebar.write("Faça o seu Login.")

#Usuário
usuario = st.sidebar.text_input(
    label="Usuário:",
    placeholder= "Digite seu usuário"
)

#Senha
senha = st.sidebar.text_input(
    label="Senha:",
    placeholder= "Digite sua senha",
    type="password"
)

#Login
confirmar = st.sidebar.checkbox(
label="Confirmar"
)

if(confirmar == True and UserController().check_login(usuario, senha) == True):
    st.title("Bem Vindo!")

    st.sidebar.success("Usuário Logado!")
    tab1, tab2, tab3 = st.tabs(["Esportes🏃‍♂️", "Aventura🐱‍🏍", "Carrinho🛒"])

    #Aba para jogos de esportes
    with tab1:
        col1, col2, col3 = st.columns(3)

        #FIFA22
        with col1:
            st.text(ProductController().get_nome("Fifa 22"))

            try:
                st.image(
                    image="assets/fifa22.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Fifa 22"))
            
            fifa_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=1
            )
        
        #FORZA
        with col2:
            st.text(ProductController().get_nome("Forza Horizon 5"))

            try:
                st.image(
                    image="assets/forza.jpg",
                    width=198
                    )
            except:
                st.text("Erro:Imagem não disponível")   

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Forza Horizon 5"))

            forza_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=2
            )

        #NFL
        with col3:
            st.text(ProductController().get_nome("Madden 22"))

            try:
                st.image(
                    image="assets/nfl.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Madden 22"))
            
            nfl_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=3
            )

    #Aba para jogos de Aventura
    with tab2:
        col1, col2, col3 = st.columns(3)

        #THE LAST OF US
        with col1:
            st.text(ProductController().get_nome("The Last of Us 2"))

            try:
                st.image(
                    image="assets/thelast.jpg",
                    width=180
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("The Last of Us 2"))
            
            thelast_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=4
            )
        
        #TOMB RAIDER
        with col2:
            st.text(ProductController().get_nome("Shadow of the Tomb Raider"))

            try:
                st.image(
                    image="assets/tomb.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Shadow of the Tomb Raider"))
            
            tomb_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=5
            )
        
        #RED DEAD REDEMPTION
        with col3:
            st.text(ProductController().get_nome("Red Dead Redemption II"))

            try:
                st.image(
                    image="assets/reddead.jpg",
                    width=195
                    )
            except:
                st.text("Erro:Imagem não disponível")

            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Red Dead Redemption II"))
            
            reddead_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=6
            )

    with tab3:

        st.warning("Para remover itens do carrinho, basta desmarcar a checkbox do item desejado em sua página.")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Itens em seu carrinho:")

            valor_total = 0

            if(fifa_button == True):
                fifa = ProductController().carrinho("Fifa 22")
                valor_total += ProductController().get_price("Fifa 22")

            if(forza_button == True):
                forza = ProductController().carrinho("Forza Horizon 5")
                valor_total += ProductController().get_price("Forza Horizon 5")

            if(nfl_button == True):
                nfl = ProductController().carrinho("Madden 22")
                valor_total += ProductController().get_price("Madden 22")

            if(thelast_button == True):
                thelast = ProductController().carrinho("The Last of Us 2")
                valor_total += ProductController().get_price("The Last of Us 2")

            if(tomb_button == True):
                tomb = ProductController().carrinho("Shadow of the Tomb Raider")
                valor_total += ProductController().get_price("Shadow of the Tomb Raider")

            if(reddead_button == True):
                redead = ProductController().carrinho("Red Dead Redemption II")
                valor_total += ProductController().get_price("Red Dead Redemption II")
            
        with col2:

            st.metric("Valor Total (R$):", valor_total) 
            st.button(label="Fazer Pagamento")
            
elif(confirmar == True and UserController().check_login(usuario, senha) == False):
    st.sidebar.error("Login incorreto, tente novamente.")
    st.warning("Insira seu usuário e senha. Marque a checkbox para validar.")
    st.warning("Para deslogar, basta desmarcar a checkbox.")

else:       
    st.warning("Insira seu usuário e senha. Marque a checkbox para validar.")
    st.warning("Para deslogar, basta desmarcar a checkbox.")