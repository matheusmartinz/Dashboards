import streamlit as st

def inject_css():
    st.markdown("""
        <style>
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
        </style>
    """, unsafe_allow_html=True)
