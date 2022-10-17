import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController

################################
#NOME: Gabriel dos Santos Couto#
#RA: 20.00273-4                #
################################

st.set_page_config(page_title="Loja Online", page_icon="🎮")

##########################
#Área de Login na sidebar#
##########################

st.sidebar.title("Faça seu login para acessar os recursos da loja!😁")
st.sidebar.write("Faça o seu Login.")

#########
#Usuário#
#########

usuario = st.sidebar.text_input(
    label="Usuário:",
    placeholder= "Digite seu usuário",
    value="Couto"
)

#######
#Senha#
#######

senha = st.sidebar.text_input(
    label="Senha:",
    placeholder= "Digite sua senha",
    type="password",
    value="1234"
)

#######
#Login#
#######

confirmar = st.sidebar.checkbox(
label="Confirmar"
)

if(confirmar == True and UserController().check_login(usuario, senha) == True):
    st.title("Bem Vindo ao mundo Pokemon!")

    st.sidebar.success("Usuário Logado!")
    tab1, tab2, tab3, tab4 = st.tabs(["Boosters", "Cards Avulsos", "Acessórios", "Carrinho 🛒"])

    ###################
    #Aba para Boosters#
    ###################

    with tab1:
        col1, col2, col3 = st.columns(3)

        
        with col1:

            #################
            #ESPADA E ESCUDO#
            #################

            st.text(ProductController().get_nome("Booster Espada e Escudo"))

            try:
                st.image(
                    image="assets/EspadaEscudo.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Booster Espada e Escudo"))
            
            EE_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=1
            )

            #############
            #TRIPLE PACK#
            #############

            st.text(ProductController().get_nome("Triple Pack Pokemon Go"))

            try:
                st.image(
                    image="assets/TriplePack.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Triple Pack Pokemon Go"))
            
            TP_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=2
            )
        
        with col2:

            ####
            #XY#
            ####

            st.text(ProductController().get_nome("Booster XY"))

            try:
                st.image(
                    image="assets/XY.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")   

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Booster XY"))

            XY_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=3
            )

            #############
            #QUADRI PACK#
            #############

            st.text(ProductController().get_nome("Quadri Pack Golpe Fusão"))

            try:
                st.image(
                    image="assets/QuadriPack.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")   

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Quadri Pack Golpe Fusão"))

            QP_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=4
            )

        with col3:

            ################
            #ORIGEM PERDIDA#
            ################

            st.text(ProductController().get_nome("Booster Origem Perdida"))

            try:
                st.image(
                    image="assets/OrigemPerdida.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Booster Origem Perdida"))
            
            OP_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=5
            )
            ###############
            #BLACK & WHITE#
            ###############

            st.text(ProductController().get_nome("Booster Black & White"))

            try:
                st.image(
                    image="assets/BlackWhite.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Booster Black & White"))
            
            BW_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=6
            )

    #########################
    #Aba para Cartas avulsas#
    #########################

    with tab2:
        col1, col2, col3 = st.columns(3)

        with col1:

            #######################
            #Giratina V-ASTRO GOLD# 
            #######################

            st.text(ProductController().get_nome("Giratina V-ASTRO Gold"))

            try:
                st.image(
                    image="assets/giratina.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Giratina V-ASTRO Gold"))
            
            GG_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=7
            )

            #########
            #Pikachu#
            #########
            st.text(ProductController().get_nome("Pikachu"))

            try:
                st.image(
                    image="assets/pikachu.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Pikachu"))
            
            PK_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=8
            )

        with col2:

            #########################
            #Samurot V-ASTRO RAINBOW#
            #########################

            st.text(ProductController().get_nome("Samurot V-ASTRO Rainbow"))

            try:
                st.image(
                    image="assets/samurott.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Samurot V-ASTRO Rainbow"))
            
            SR_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=9
            )

            #################
            #Gengar Full Art# 
            #################
            st.text(ProductController().get_nome("Gengar Full Art"))

            try:
                st.image(
                    image="assets/gengar.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Gengar Full Art"))
            
            GF_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=10
            )

        with col3:

            ##########
            #Mewtwo V#
            ##########

            st.text(ProductController().get_nome("Mewtwo V"))

            try:
                st.image(
                    image="assets/mewtwo.jpg",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Mewtwo V"))
            
            MV_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=11
            )

            ###########
            #Charizard#
            ###########

            st.text(ProductController().get_nome("Charizard"))

            try:
                st.image(
                    image="assets/charizard.png",
                    width=200
                    )
            except:
                st.text("Erro:Imagem não disponível")

            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Charizard"))
            
            CH_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=12
            )

    #####################
    #Aba para Acessórios#
    #####################

    with tab3:
        col1, col2, col3 = st.columns(3)

        ###############
        #FICHÁRIO AZUL#
        ###############

        with col1:
            st.text(ProductController().get_nome("Fichário Azul"))

            try:
                st.image(
                    image="assets/FicharioAzul.jpg",
                    width=180
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Fichário Azul"))
            
            FA_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=13
            )
        
        ########
        #SLEEVE#
        ########

        with col2:
            st.text(ProductController().get_nome("Sleeve Básica"))

            try:
                st.image(
                    image="assets/SleeveBasica.jpg",
                    width=180
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Sleeve Básica"))
            
            SB_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=14
            )
        with col3:

            ##################
            #SLEEVE CHARIZARD#
            ##################

            st.text(ProductController().get_nome("Sleeve Charizard"))

            try:
                st.image(
                    image="assets/SleevePersonalizada.jpg",
                    width=180
                    )
            except:
                st.text("Erro:Imagem não disponível")
            
            st.metric(
                label="Preço (R$):",
                value=ProductController().get_price("Sleeve Charizard"))
            
            SC_button = st.checkbox(
                label="Adicionar ao carrinho",
                key=15
            )

    ####################
    #Página de Carrinho#
    ####################

    with tab4:

        st.warning("Para remover itens do carrinho, basta desmarcar a checkbox do item desejado em sua página.")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Itens em seu carrinho:")

            valor_total = 0

            if(EE_button == True):
                EE = ProductController().carrinho("Booster Espada e Escudo")
                valor_total += ProductController().get_price("Booster Espada e Escudo")

            if(XY_button == True):
                XY = ProductController().carrinho("Booster XY")
                valor_total += ProductController().get_price("Booster XY")

            if(OP_button == True):
                OP = ProductController().carrinho("Booster Origem Perdida")
                valor_total += ProductController().get_price("Booster Origem Perdida")

            if(TP_button == True):
                TP = ProductController().carrinho("Triple Pack Pokemong Go")
                valor_total += ProductController().get_price("Triple Pack Pokemong Go")

            if(QP_button == True):
                QP = ProductController().carrinho("Quadri Pack Golpe Fusão")
                valor_total += ProductController().get_price("Quadri Pack Golpe Fusão")

            if(BW_button == True):
                BW = ProductController().carrinho("Booster Black & White")
                valor_total += ProductController().get_price("Booster Black & White")
            
            if(GG_button == True):
                GG = ProductController().carrinho("Giratina V-ASTRO Gold")
                valor_total += ProductController().get_price("Giratina V-ASTRO Gold")
            
            if(PK_button == True):
                PK = ProductController().carrinho("Pikachu")
                valor_total += ProductController().get_price("Pikachu")
            
            if(SR_button == True):
                SR = ProductController().carrinho("Samurot V-ASTRO Rainbow")
                valor_total += ProductController().get_price("Samurot V-ASTRO Rainbow")
            
            if(GF_button == True):
                GF = ProductController().carrinho("Gengar Full Art")
                valor_total += ProductController().get_price("Gengar Full Art")
            
            if(MV_button == True):
                MV = ProductController().carrinho("Mewtwo V")
                valor_total += ProductController().get_price("Mewtwo V")
            
            if(CH_button == True):
                CH = ProductController().carrinho("Charizard")
                valor_total += ProductController().get_price("Charizard")

            if(FA_button == True):
                FA = ProductController().carrinho("Fichário Azul")
                valor_total += ProductController().get_price("Fichário Azul")
            
            if(SB_button == True):
                SB = ProductController().carrinho("Sleeve Básica")
                valor_total += ProductController().get_price("Sleeve Básica")

            if(SC_button == True):
                SC = ProductController().carrinho("Sleeve Charizard")
                valor_total += ProductController().get_price("Sleeve Charizard")
            
        with col2:

            #########################
            #Pagamento - Preço total#
            #########################
            st.metric("Valor Total (R$):", round((valor_total),2)) 
            st.button(label="Fazer Pagamento")

###############
#Erro de login# 
###############
           
elif(confirmar == True and UserController().check_login(usuario, senha) == False):
    st.sidebar.error("Login incorreto, tente novamente.")
    st.warning("Insira seu usuário e senha. Marque a checkbox para validar.")
    st.warning("Para deslogar, basta desmarcar a checkbox.")

#################
#Mensagem Padrão#
#################

else:       
    st.warning("Insira seu usuário e senha. Marque a checkbox para validar.")
    st.warning("Para deslogar, basta desmarcar a checkbox.")