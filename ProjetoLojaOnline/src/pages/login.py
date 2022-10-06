from email.policy import default
import streamlit as st
#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

#Configuraçã da pagina
st.set_page_config(page_title="Login", page_icon="✔")

#Título
st.title("Faça o seu Login")

#Usuário
usuario = st.text_input(
    label="Usuário:",
    placeholder= "Digite seu usuário"
)

#Senha
senha = st.text_input(
    label="Senha:",
    placeholder= "Digite sua senha",
    type="password" 
)

#Login
confirmar = st.button(
    label="Confirmar"
)