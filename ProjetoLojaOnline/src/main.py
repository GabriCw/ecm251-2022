import streamlit as st
#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

#Rodar usando python -m streamlit run ./src/main.py

#Configuraçã da pagina
st.set_page_config(page_title="Bem Vindo", page_icon="✨")

#Título
st.title("Loja Online")

#Texto apresentação
st.text("Seja bem vindo a nossa loja!")

#Logo da loja
st.image(
    image="assets/logo.jpg",
    width=350
    )

#Texto sobre entrar
st.text("Clique o botão abaixo para entrar.")

#Botão para entrar na tela de login
entrar = st.button(
    label="Entrar"
)