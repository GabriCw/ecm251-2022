import streamlit as st
#NOME: Gabriel dos Santos Couto
#RA: 20.00273-4

st.title("Jogos")
tab1, tab2 = st.tabs(["Esportes", "Aventura"])

#Aba para jogos de esportes
with tab1:
    col1, col2, col3 = st.columns(3)

    #FIFA22
    with col1:
        st.text("Fifa 22")
        st.image(
            image="assets/fifa22.jpg",
            width=200
            )

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
        st.image(
            image="assets/forza.jpg",
            width=198
            )
        
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
        st.image(
            image="assets/nfl.jpg",
            width=200
            )
        
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
        st.image(
            image="assets/thelast.jpg",
            width=180
            )
        
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
        st.image(
            image="assets/tomb.jpg",
            width=200
            )
        
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
        st.image(
            image="assets/reddead.jpg",
            width=195
            )
        
        st.metric(
            label="Preço:",
            value="R$ 200.00")
        
        reddead_button = st.button(
            label="Adicionar ao carrinho",
            key=6
        )