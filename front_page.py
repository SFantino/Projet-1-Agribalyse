import streamlit as st

def apply_custom_design():
    """
    Applique le CSS personnalisé pour l'interface Streamlit.
    """
    custom_css = """
    <style>
    /* Bandeau de navigation */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #e8e8e8;
        padding: 10px 0;
        z-index: 1000;
        display: flex;
        justify-content: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Contenu du bandeau */
    .navbar a {
        color: black;
        text-decoration: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Hover sur les liens */
    .navbar a:hover {
        background-color: #d6d6d6;
    }

    /* Conteneur des menus déroulants */
    .dropdown {
        position: relative;
        display: inline-block;
    }

    /* Contenu des sous-menus */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #e8e8e8;
        min-width: 200px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Sous-menus visibles au survol */
    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* Style des sous-menus */
    .dropdown-content a {
        display: block;
        padding: 10px;
        text-decoration: none;
        color: black;
        font-size: 16px;
    }

    /* Suppression du fond bleu et du soulignement */
    .dropdown-content a:hover {
        background-color: #d6d6d6;
        text-decoration: none;
    }

    /* Décalage du contenu principal pour ne pas être caché sous le bandeau */
    .content {
        margin-top: 60px;
    }
    </style>
    """

    navbar_html = """
    <div class="navbar">
        <a href="/Accueil" target="_self">🏠 Accueil</a>
        
        <div class="dropdown">
            <a href="#">📖 Méthodologie</a>
            <div class="dropdown-content">
                <a href="/Methodologie" target="_self">📌 Fonctionnement général</a>
                <a href="/Normalisation" target="_self">📊 Normalisation</a>
            </div>
        </div>

        <div class="dropdown">
            <a href="#">📚 Ressources</a>
            <div class="dropdown-content">
                <a href="/Base_Agribalyse" target="_self">📂 Base de données Agribalyse</a>
                <a href="/ACV" target="_self">🌍 ACV</a>
                <a href="/Indicateurs" target="_self">📈 16 indicateurs</a>
            </div>
        </div>
    </div>

    <div class="content">
    """

    return custom_css + navbar_html
