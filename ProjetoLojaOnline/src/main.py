from fsspec import Callback
from sqlalchemy import null
import streamlit as st
from models.user import User

#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

#Criando os usuários
users = [
    User(name="Gabriel", password="3333"),
    User(name="Couto", password="1234")
    ]

def check_login(name, password):
        user_teste = User(name=name, password=password)
        for user in users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False

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

if(confirmar == True and check_login(usuario, senha) == True):
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
            
            fifa_button = st.button(
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

            forza_button = st.button(
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
            
            nfl_button = st.button(
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
            
            thelast_button = st.button(
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
            
            tomb_button = st.button(
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
            
            reddead_button = st.button(
                label="Adicionar ao carrinho",
                key=6
            )

    with tab3:
        #Titulo
        st.title("Carrinho")
        st.text("Itens em seu carrinho:")
        
        if(fifa_button):
            st.text("Fifa 22 - R$: 250.00")
            st.button(
                label="Remover"
            )

        if(forza_button):
            st.text("Forza horizon 5 - R$: 200.00")
            st.button(
                label="Remover"
            )
else:
    st.warning("Insira seu login corretamente e clique na checkbox para validar")