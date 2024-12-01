import streamlit as st
import pandas as pd

# Function to make specified columns clickable
def make_links_clickable(df, link_columns):
    for col in link_columns:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: f'<a href="{x}" target="_blank">Click here</a>' if pd.notna(x) and str(x).strip() != '' else 'No Link'
            )
    return df

# Custom CSS for centering table content
st.markdown("""
    <style>
    table {
        width: auto;
    }
    th, td {
        text-align: center !important;
        vertical-align: middle !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar page selection for navigation
page = st.sidebar.selectbox("Choose a page", ["Main Page", "Karma Star", "Tithi-Mudaku-Namayoga Palankal"])

# Header Information (shown on all pages)
st.markdown("""
    <h2 style='text-align: center; color: black;'>திதி யோக கரண ஆராய்ச்சியாளர் <br>
    கால கணித ஜோதிடர்<br> சந்திர சிவக்குமார்<br>
    கால பைரவர் ஜோதிட பவனம்<br>காடையாம்பட்டி வட்டம்<br>சேலம் மாவட்டம்</h2>
    <h3 style='text-align: center; color: black;'>Cell: +91 8883113734</h3>
""", unsafe_allow_html=True)

# User name input
user_name = st.sidebar.text_input("Enter your name:")

# Display the entered name in the main section
if user_name:
    st.markdown(f"<h3 style='text-align: center; color: black;'>ஜாதகர், {user_name}, வழிபடவேண்டிய கோவில்கள்!</h3>", unsafe_allow_html=True)

# Main Page Logic
if page == "Main Page":
    tithi_type = st.sidebar.selectbox("திதி", ['வளர்பிறை திதி', 'தேய்பிறை திதி'])

    # Load data based on Tithi type
    file_name = "mohan01.xlsx" if tithi_type == 'வளர்பிறை திதி' else "mohan02.xlsx"
    try:
        df = pd.read_excel(file_name, engine="openpyxl")
        st.markdown(f"<h2 style='text-align: center; color: black;'>{tithi_type}</h2>", unsafe_allow_html=True)
        tithi = st.sidebar.selectbox('திதி', df.iloc[:, 0].dropna().unique())
        selected_tithi_df = df[df.iloc[:, 0] == tithi].copy()
        selected_tithi_df = make_links_clickable(selected_tithi_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
        st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading data: Please check the Excel file.")

# Karma Star Page Logic
elif page == "Karma Star":
    try:
        dfa = pd.read_excel("karma_star.xlsx", engine="openpyxl")
        kar = st.sidebar.multiselect('கர்ம நட்சத்திரம்', dfa['கர்ம நட்சத்திரம்'].unique())
        selected_kar_df = dfa[dfa['கர்ம நட்சத்திரம்'].isin(kar)].copy() if kar else pd.DataFrame()
        selected_kar_df = make_links_clickable(selected_kar_df, ['இணையதள இணைப்பு'])
        st.markdown(selected_kar_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading Karma Star data.")

# Tithi-Mudaku-Namayoga Palankal Page Logic
elif page == "Tithi-Mudaku-Namayoga Palankal":
    try:
        df = pd.read_excel("thithi_palankal.xlsx", engine="openpyxl")
        tithi = st.sidebar.selectbox('திதி', df.iloc[:, 0].dropna().unique())
        selected_tithi_df = df[df.iloc[:, 0] == tithi].copy()
        selected_tithi_df = make_links_clickable(selected_tithi_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
        st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading Tithi data.")

    try:
        df1 = pd.read_excel("mudakku-palangal.xlsx", engine="openpyxl")
        mudaku = st.sidebar.selectbox('முடக்கு பாவகம்', df1.iloc[:, 0].dropna().unique())
        selected_mudakku_df = df1[df1.iloc[:, 0] == mudaku].copy()
        selected_mudakku_df = make_links_clickable(selected_mudakku_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
        st.markdown(selected_mudakku_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading Mudakku data.")

    try:
        df2 = pd.read_excel("Namayoga Palankal.xlsx", engine="openpyxl")
        nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].dropna().unique())
        selected_namayogam_df = df2[df2.iloc[:, 0] == nam_yogam].copy()
        selected_namayogam_df = make_links_clickable(selected_namayogam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
        st.markdown(selected_namayogam_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading Namayogam data.")
