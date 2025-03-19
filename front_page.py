import streamlit as st

def show_navbar():
    st.markdown("""
    <div class="navbar">
        <a href="/?page=home">🏠 Accueil</a>

        <div class="dropdown">
            <a href="#">📖 Méthodologie</a>
            <div class="dropdown-content">
                <a href="/?page=fonctionnement">📌 Fonctionnement général</a>
                <a href="/?page=normalisation">📊 Normalisation</a>
            </div>
        </div>

        <div class="dropdown">
            <a href="#">📚 Ressources</a>
            <div class="dropdown-content">
                <a href="/?page=agribalyse">📂 Base de données Agribalyse</a>
                <a href="/?page=acv">🌍 ACV</a>
                <a href="/?page=indicateurs">📈 16 indicateurs</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
