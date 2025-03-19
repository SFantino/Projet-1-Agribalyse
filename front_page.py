import streamlit as st

def show_navbar():
    st.markdown(
        """
        <style>
        .menu-container {
            background-color: #e8e8e8;
            padding: 10px;
            display: flex;
            justify-content: center;
            border-bottom: 2px solid #ccc;
        }
        .menu-item {
            margin: 0 15px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            color: black;
            position: relative;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 200px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            z-index: 1;
        }
        .menu-item:hover .dropdown-content {
            display: block;
        }
        .dropdown-item {
            padding: 10px;
            color: black;
            text-decoration: none;
            display: block;
            font-size: 16px;
        }
        .dropdown-item:hover {
            background-color: #ddd;
        }
        </style>
        <div class="menu-container">
            <div class="menu-item" onclick="window.location.href='/'">Accueil</div>
            <div class="menu-item">
                Méthodologie
                <div class="dropdown-content">
                    <a class="dropdown-item" href="?page=fonctionnement">🔹 Fonctionnement général</a>
                    <a class="dropdown-item" href="?page=normalisation">🔹 Normalisation</a>
                </div>
            </div>
            <div class="menu-item">
                Ressources
                <div class="dropdown-content">
                    <a class="dropdown-item" href="?page=agribalyse">📊 Base de données Agribalyse</a>
                    <a class="dropdown-item" href="?page=acv">♻️ ACV</a>
                    <a class="dropdown-item" href="?page=indicateurs">📈 16 indicateurs</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def get_selected_page():
    """ Récupère la page sélectionnée à partir de l'URL """
    return st.experimental_get_query_params().get("page", [""])[0]
