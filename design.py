def apply_custom_design():
    """
    Applique le CSS personnalisé pour l'interface Streamlit.
    """
    custom_css = """
    <style>
    /* Changer la couleur de fond de l'application */
    .stApp {
        background-color: white;
    }

    /* Changer la couleur du texte général */
    .stMarkdown, .stTextInput, .stSelectbox, .stButton, .stDataFrame, .stRadio, .stTitle, .stHeader {
        color: black !important;
    }

    /* Changer la couleur des titres */
    h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }

    /* Personnaliser les barres de recherche */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #e8e8e8 !important;
        color: black !important;
    }

    /* Personnaliser les boutons */
    .stButton>button {
        background-color: #e8e8e8 !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }

    /* Personnaliser les zones de sélection (selectbox) */
    .stSelectbox>div>div>div {
        background-color: #e8e8e8 !important;
        color: black !important;
    }
    </style>
    """
    return custom_css
