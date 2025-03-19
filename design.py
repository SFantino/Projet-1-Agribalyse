def apply_custom_design():
    return """
    <style>
        /* Bandeau de navigation */
        .navbar {
            background-color: #e8e8e8;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-around;
            padding: 0 20px;
            font-size: 18px;
            font-family: Arial, sans-serif;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }

        .navbar a {
            color: black;
            text-decoration: none;
            padding: 10px 15px;
            transition: background-color 0.3s;
        }

        .navbar a:hover {
            background-color: #d6d6d6;
            border-radius: 5px;
        }

        /* Menu déroulant */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 220px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            border-radius: 5px;
        }

        .dropdown-content a {
            color: black;
            padding: 10px 15px;
            display: block;
        }

        .dropdown-content a:hover {
            background-color: #e0e0e0;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        /* Décaler le contenu principal sous le bandeau */
        .content {
            margin-top: 80px;
        }
    </style>
    """
