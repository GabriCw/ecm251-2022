import streamlit as st
#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

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
    placeholder= "Digite sua senha"
)

#Login
confirmar = st.button(
    label="Confirmar"
)