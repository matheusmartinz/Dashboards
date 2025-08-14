import streamlit as st

def inject_css():
    st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #FEFAE0 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
            html, body, .main, .block-container, .stHeader {
                background-color: #FEFAE0 !important;
            }
            .stApp, .stHeader {
                background-color: #FEFAE0 !important;
            }
            .stAppHeader {
                background-color: #FEFAE0 !important;
            }
            .main {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 0.5rem;
                padding-bottom: 0.5rem;
            }

            ::-webkit-scrollbar {
                display: none;
            }

            .block-container {
                padding: 1rem 1rem 1rem 1rem !important;
                margin: 0 !important;
                max-width: 100% !important;
            }

            .element-container {
                padding: 0 !important;
                margin: 0 !important;
            }
            
            
            .title-custom {
                text-align: center;
                color: #000000;  /* Cor laranja tom tomate, altere conforme necessidade */
                font-size: 36px;
                font-weight: bold;
                margin-top: 20px
            }

            .st-emotion-cache-17fc32d {
                color: black !important
            }
            .stSidebar {
                background-color: #FEFAE0 !important;  
            }
            .stSidebarContent {
                background-color: #FF6347 !important;  /* Cor de fundo do menu */
            }
            
            .stException {
                color: #FFFFFF !important;  /* Cor do texto de erro */
                background-color: #D32F2F !important;  /* Cor de fundo do erro (vermelho) */
                border: 1px solid #9C2A2A !important;  /* Borda vermelha */
                padding: 10px !important;  /* Espaçamento interno */
                font-weight: bold !important;  /* Negrito no texto */
                border-radius: 5px !important;  /* Bordas arredondadas */
             },
    """, unsafe_allow_html=True)


