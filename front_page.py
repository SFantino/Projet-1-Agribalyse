import streamlit as st

def show_navbar():
    """
    Affiche la barre de navigation en haut de la page.
    """
    navbar_html = """
    <style>
    /* Fixe le menu en haut */
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
        align-items: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Style des liens */
    .navbar a {
        color: black;
        text-decoration: none;
        padding: 15px 20px;
        font-size: 20px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }

    /* Effet au survol */
    .navbar a:hover {
        background-color: #d6d6d6;
    }

    /* Style des menus déroulants */
    .dropdown {
        position: relative;
        display: inline-block;
    }

    /* Contenu des sous-menus */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #e8e8e8;
        min-width: 250px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
    }

    /* Affichage du sous-menu au survol */
    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* Style des liens dans le sous-menu */
    .dropdown-content a {
        display: block;
        padding: 12px 15px;
        color: black;
        font-size: 18px;
        text-decoration: none;
    }

    /* Suppression du fond bleu et du soulignement */
    .dropdown-content a:hover {
        background-color: #d6d6d6;
        text-decoration: none;
    }

    /* Décalage du contenu pour éviter qu'il soit caché sous le bandeau */
    .content {
        margin-top: 70px;
    }
    </style>

    <div class="navbar">
        <a href="/?page=accueil">🏠 Accueil</a>
        
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
    """

    st.markdown(navbar_html, unsafe_allow_html=True)

def get_selected_page():
    query_params = st.query_params
    return query_params.get("page", "accueil")
