import streamlit as st
#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

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