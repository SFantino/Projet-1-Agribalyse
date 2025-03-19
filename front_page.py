import streamlit as st

def custom_css():
    return """
    <style>
        /* Style général du bandeau */
        .topnav {
            background-color: #e8e8e8;
            overflow: hidden;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 10px 0;
            z-index: 1000;
        }
        
        /* Conteneur centré */
        .nav-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
        }

        /* Style des liens du menu */
        .nav-item {
            font-size: 18px;
            font-weight: bold;
            color: black;
            text-decoration: none;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }

        .nav-item:hover {
            background-color: #dcdcdc;
            border-radius: 5px;
        }

        /* Style du menu déroulant */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: white;
            min-width: 200px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            border-radius: 5px;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        /* Style des sous-menus */
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            font-size: 16px;
        }

        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }

        /* Espacement pour éviter que le contenu soit caché par le bandeau */
        .content {
            margin-top: 60px;
        }
    </style>
    """

def render_navbar():
    st.markdown(custom_css(), unsafe_allow_html=True)
    st.markdown("""
        <div class="topnav">
            <div class="nav-container">
                <a href="?page=Accueil" class="nav-item">Accueil</a>

                <div class="dropdown">
                    <a class="nav-item">Méthodologie</a>
                    <div class="dropdown-content">
                        <a href="?page=Fonctionnement">🛠️ Fonctionnement général</a>
                        <a href="?page=Normalisation">📏 Normalisation</a>
                    </div>
                </div>

                <div class="dropdown">
                    <a class="nav-item">Ressources</a>
                    <div class="dropdown-content">
                        <a href="?page=Base">📊 Base de données Agribalyse</a>
                        <a href="?page=ACV">🌍 ACV</a>
                        <a href="?page=Indicateurs">📈 16 indicateurs</a>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_page():
    query_params = st.experimental_get_query_params()
    return query_params.get("page", ["Accueil"])[0]

def load_page():
    page = get_page()
    
    if page == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        # Ici, tu peux importer Test1.py uniquement pour la page d'accueil
        import Test1

    elif page == "Fonctionnement":
        st.title("Méthodologie - Fonctionnement général")
        st.write("Contenu sur le fonctionnement général.")

    elif page == "Normalisation":
        st.title("Méthodologie - Normalisation")
        st.write("Contenu sur la normalisation.")

    elif page == "Base":
        st.title("Ressources - Base de données Agribalyse")
        st.write("Informations sur Agribalyse.")

    elif page == "ACV":
        st.title("Ressources - ACV")
        st.write("Explication sur l'Analyse de Cycle de Vie.")

    elif page == "Indicateurs":
        st.title("Ressources - 16 indicateurs")
        st.write("Détails sur les 16 indicateurs environnementaux.")

# Affichage du bandeau de navigation
render_navbar()

# Chargement de la page sélectionnée
load_page()
