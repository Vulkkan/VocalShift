# styles.py
def custom_css():
    return """
        <style>
        [data-testid="stDecoration"] {
            background: #FFFFFF;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            background: -webkit-linear-gradient(270deg, #00051DFF, #001C97FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: -40px;
        }
        .subtitle-bold {
            font-size: 24px;
            font-weight: bold;
            background: black;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: -15px;
        }
        .subtitle {
            font-size: 16px;
            font-weight: normal;
            background: black;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Custom radio button styles */
        div.stRadio > label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }

        .stButton > button {
            color: white;
            border-radius: 12px;
            font-size: 14px;
            font-weight: bold;
            padding: 2px 4px;
            border: none;
            width: 120px;
            transition: 0.3s ease;
            transform: skew(-10deg);
        }
        .stButton > button-content {
            transform: skew(10deg);
        }
        div.stButton > button:first-child:hover {
            background: linear-gradient(to right, #2B4CE1FF, #6480FFFF);
            transform: scale(1.05);
        }
    </style>
    """
