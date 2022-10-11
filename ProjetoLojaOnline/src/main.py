from regex import F
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController

#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

#Área de Login na sidebar
st.sidebar.title("Faça seu login para acessar os recursos da loja😁")
st.sidebar.write("Faça o seu Login")

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

    tab1, tab2, tab3 = st.tabs(["Esportes", "Aventura", "Carrinho"])

    #Aba para jogos de esportes
    with tab1:
        col1, col2, col3 = st.columns(3)

        #FIFA22
        with col1:
            st.text("Fifa 22")

            try:
                st.image(
                    image="assets/fifa22.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço:",
                value="R$ 250.00")
            
            fifa_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=1
            )
        
        #FORZA
        with col2:
            st.text("Forza Horizon 5")

            try:
                st.image(
                    image="assets/forza.jpg",
                    width=198
                    )
            except:
                st.text("Erro:Imagem não disponível")   

            st.metric(
                label="Preço:",
                value="R$ 200.00")

            forza_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=2
            )

        #NFL
        with col3:
            st.text("Madden 22")

            try:
                st.image(
                    image="assets/nfl.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço:",
                value="R$ 250.00")
            
            nfl_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=3
            )

    #Aba para jogos de Aventura
    with tab2:
        col1, col2, col3 = st.columns(3)

        #THE LAST OF US
        with col1:
            st.text("The Last of Us 2")

            try:
                st.image(
                    image="assets/thelast.jpg",
                    width=180
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço:",
                value="R$ 250.00")
            
            thelast_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=4
            )
        
        #TOMB RAIDER
        with col2:
            st.text("Shadow of the Tomb Raider")

            try:
                st.image(
                    image="assets/tomb.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço:",
                value="R$ 150.00")
            
            tomb_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=5
            )
        
        #RED DEAD REDEMPTION
        with col3:
            st.text("Red Dead Redemption II")

            try:
                st.image(
                    image="assets/reddead.jpg",
                    width=195
                    )
            except:
                st.text("Erro:Imagem não disponível")

            
            st.metric(
                label="Preço:",
                value="R$ 200.00")
            
            reddead_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=6
            )

    with tab3:

        st.title("Carrinho")
        st.warning("Para remover itens do carrinho, basta desclicar a checkbox do item")
        st.text("Itens em seu carrinho:")
        
        if(fifa_button == True):
            fifa = ProductController().carrinho("Fifa 22", "250.00")

        if(forza_button == True):
            forza = ProductController().carrinho("Forza Horizon 5", "200.00")

        if(nfl_button == True):
            nfl = ProductController().carrinho("Madden 22", "250.00")

        if(thelast_button == True):
            thelast = ProductController().carrinho("The Last of Us 2", "250.00")

        if(tomb_button == True):
            tomb = ProductController().carrinho("Shadow of the Tomb Raider", "150.00")
        
        if(reddead_button == True):
            redead = ProductController().carrinho("Red Dead Redemption II", "200.00")

            
                
else:
    st.warning("Insira seu login corretamente e clique na checkbox para validar")