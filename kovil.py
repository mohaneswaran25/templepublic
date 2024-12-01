import streamlit as st
import pandas as pd

# Function to make specified columns clickable
def make_links_clickable(df, link_columns):
    for col in link_columns:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: f'<a href="{x}" target="_blank">Click here</a>' if pd.notna(x) and x.strip() != '' else '<a href="#">No Link</a>'
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
page = st.sidebar.selectbox("Choose a page", ["Main Page", "Karma Star", "thiti-mudaku-Namayoga Palankal"])

# Header Information (shown on both pages)
st.markdown(
    "<h2 style='text-align: center; color: black;'>திதி யோக கரண ஆராய்ச்சியாளர் <br>கால கணித ஜோதிடர்<br> சந்திர சிவக்குமார்<br>கால பைரவர் ஜோதிட பவனம்<br>காடையாம்பட்டி வட்டம் <br> சேலம் மாவட்டம்</h2><h3 style='text-align: center; color: black;'>Cell: +91 8883113734</h3>",
    unsafe_allow_html=True
)

# Add text input for the user's name
user_name = st.sidebar.text_input("Enter your name:")

# Display the entered name in the main section if provided
if user_name:
    st.markdown(f"<h3 style='text-align: center; color: black;'>ஜாதகர், {user_name}, வழிபடவேண்டிய கோவில்கள்!</h3>", unsafe_allow_html=True)

# Main Page Content
if page == "Main Page":
    import streamlit as st
import pandas as pd

# Function to make specified columns clickable
def make_links_clickable(df, link_columns):
    for col in link_columns:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: f'<a href="{x}" target="_blank">Click here</a>' if pd.notna(x) and x.strip() != '' else '<a href="#">No Link</a>'
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
page = st.sidebar.selectbox("Choose a page", ["Main Page", "Karma Star", "thiti-mudaku-Namayoga Palankal"])

# Header Information (shown on both pages)
st.markdown(
    "<h2 style='text-align: center; color: black;'>திதி யோக கரண ஆராய்ச்சியாளர் <br>கால கணித ஜோதிடர்<br> சந்திர சிவக்குமார்<br>கால பைரவர் ஜோதிட பவனம்<br>காடையாம்பட்டி வட்டம் <br> சேலம் மாவட்டம்</h2><h3 style='text-align: center; color: black;'>Cell: +91 8883113734</h3>",
    unsafe_allow_html=True
)

# Add text input for the user's name
user_name = st.sidebar.text_input("Enter your name:")

# Display the entered name in the main section if provided
if user_name:
    st.markdown(f"<h3 style='text-align: center; color: black;'>ஜாதகர், {user_name}, வழிபடவேண்டிய கோவில்கள்!</h3>", unsafe_allow_html=True)

# Main Page Content
if page == "Main Page":
    # Angusunaathar Section
    st.markdown("<h2 style='text-align: center; color: black;'>அங்குசுநாதர் தகவல்</h2>", unsafe_allow_html=True)
    
    # Load Angusunaathar data
    df = pd.read_excel("angusunaathar.xlsx", engine="openpyxl")
    #angusunaathar_df = make_links_clickable(angusunaathar_data, ["Website Links"])

    # Display data in dropwn
    selected_angusunaathar = st.sidebar.selectbox('அங்குசுநாதர்', df.iloc[:, 0].values)
    
    # Filter and display selected data
    selected_angusunaathar_df = df[df.iloc[:, 0] == selected_angusunaathar].copy()
    selected_angusunaathar_df = make_links_clickable(selected_angusunaathar_df, ['Website Links'])
    st.markdown(selected_angusunaathar_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Sidebar selection for Tithi
    tithi_type = st.sidebar.selectbox("திதி", ('வளர்பிறை திதி', 'தேய்பிறை திதி'))

    # Load respective data based on Tithi type
    if tithi_type == 'வளர்பிறை திதி':
        df = pd.read_excel("mohan01.xlsx", engine="openpyxl")
        st.markdown("<h2 style='text-align: center; color: black;'>வளர்பிறை திதி</h2>", unsafe_allow_html=True)
    else:
        df = pd.read_excel("mohan02.xlsx", engine="openpyxl")
        st.markdown("<h2 style='text-align: center; color: black;'>தேய்பிறை திதி</h2>", unsafe_allow_html=True)

    # Tithi selection with clickable link
    tithi = st.sidebar.selectbox('திதி', df.iloc[:, 0].values)
    selected_tithi_df = df[df.iloc[:, 0] == tithi].copy()
    selected_tithi_df = make_links_clickable(selected_tithi_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Namayogam section
    st.markdown("<h2 style='text-align: center; color: black;'>நாம யோகங்கள்</h2>", unsafe_allow_html=True)
    df2 = pd.read_excel("mohan03.xlsx", engine="openpyxl")
    nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].values)
    selected_namayogam_df = df2[df2.iloc[:, 0] == nam_yogam].copy()
    selected_namayogam_df = make_links_clickable(selected_namayogam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])

    # Split and display the DataFrame sections
    first_part = selected_namayogam_df.iloc[:, :5]
    second_part = selected_namayogam_df.iloc[:, 5:]
    combined_df = pd.concat([selected_namayogam_df.iloc[:, :1], second_part], axis=1)

    st.markdown(first_part.to_html(escape=False, index=False), unsafe_allow_html=True)
    st.markdown(combined_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Mudakku section
    st.markdown("<h2 style='text-align: center; color: black;'>முடக்கு</h2>", unsafe_allow_html=True)
    df3 = pd.read_excel("mohan04.xlsx", engine="openpyxl")
    mudakku = st.sidebar.selectbox('முடக்கு', df3['முடக்கு பாவகம் '].unique())
    mudakku_rasi = st.sidebar.multiselect("முடக்கு ராசி/கிரகம்", df3['முடக்கு ராசி/கிரகம்'].unique())

    if mudakku_rasi:
        selected_mudakku_df = df3[(df3['முடக்கு பாவகம் '] == int(mudakku)) & (df3['முடக்கு ராசி/கிரகம்'].isin(mudakku_rasi))].copy()
    else:
        selected_mudakku_df = pd.DataFrame()

    selected_mudakku_df = make_links_clickable(selected_mudakku_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_mudakku_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Vainasikam section
    st.markdown("<h2 style='text-align: center; color: black;'>வைநாசிகம்</h2>", unsafe_allow_html=True)
    df4 = pd.read_excel("mohan05.xlsx", engine="openpyxl")
    vainasikam = st.sidebar.selectbox('வைநாசிகம்', df4.iloc[:, 0].values)
    selected_vainasikam_df = df4[df4.iloc[:, 0] == vainasikam].copy()
    selected_vainasikam_df = make_links_clickable(selected_vainasikam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_vainasikam_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Karanam section
    st.markdown("<h2 style='text-align: center; color: black;'>கரணம்</h2>", unsafe_allow_html=True)
    df5 = pd.read_excel("mohan06.xlsx", engine="openpyxl")
    karanam = st.sidebar.selectbox('கரணம்', df5.iloc[:, 0].values)
    selected_karanam_df = df5[df5.iloc[:, 0] == karanam].copy()
    selected_karanam_df = make_links_clickable(selected_karanam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_karanam_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Karma Star Page Content
elif page == "Karma Star":
    # Display Karma Star Section
    st.markdown("<h2 style='text-align: center; color: black;'>கர்ம நட்சத்திரம்</h2>", unsafe_allow_html=True)
    dfa = pd.read_excel("karma_star.xlsx", engine="openpyxl")
    #kar = st.sidebar.selectbox('கர்ம நட்சத்திரம்', dfa.iloc[:, 0].values)
    #selected_kar_df = dfa[dfa.iloc[:, 0] == kar].copy()
    # dfa = pd.read_excel("karma_star.xlsx", engine="openpyxl")
    kar = st.sidebar.multiselect('கர்ம நட்சத்திரம்', dfa['கர்ம நட்சத்திரம்'].unique())
    selected_kar_df = dfa[dfa['கர்ம நட்சத்திரம்'].isin(kar)].copy() if kar else pd.DataFrame()
    
    selected_kar_df = make_links_clickable(selected_kar_df, ['இணையதள இணைப்பு'])
    st.markdown(selected_kar_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    # Additional Karma Star section
    st.markdown("<h2 style='text-align: center; color: black;'>யோகாதிபதி கரணாதிபதி கர்ம நட்சத்திரத்தில் நின்றால்</h2>", unsafe_allow_html=True)
    df_karma = pd.read_excel("kar.xlsx", engine="openpyxl")
    #df_karma = pd.read_excel("kar.xlsx", engine="openpyxl")

    # Multiselect for additional Karma Star data
    karma = st.sidebar.multiselect('யோகாதிபதி கரணாதிபதி கர்ம நட்சத்திரத்தில் நின்றால்', df_karma['கர்ம நட்சத்திரம்'].unique())
    selected_karma_df = df_karma[df_karma['கர்ம நட்சத்திரம்'].isin(karma)].copy() if karma else pd.DataFrame()

    selected_karma_df = make_links_clickable(selected_karma_df, ['இணையதள இணைப்பு'])
    st.markdown(selected_karma_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    
# Yogi Palankal Page Content
elif page == "thiti-mudaku-Namayoga Palankal":
    # thiti section
    st.markdown("<h2 style='text-align: center; color: black;'>திதி பலன்கள்</h2>", unsafe_allow_html=True)
    df = pd.read_excel("thithi_palankal.xlsx", engine="openpyxl")
    nam_yogam = st.sidebar.selectbox('திதி', df.iloc[:, 0].values)
    selected_tithi_df = df[df.iloc[:, 0] == nam_yogam].copy()
    selected_tithi_df = make_links_clickable(selected_tithi_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # mudakku section
    st.markdown("<h2 style='text-align: center; color: black;'>முடக்கு பலன்கள்</h2>", unsafe_allow_html=True)
    df1 = pd.read_excel("mudakku-palangal.xlsx", engine="openpyxl")
    mudaku = st.sidebar.selectbox('முடக்கு பாவகம்', df1.iloc[:, 0].values)
    selected_mudakku_df = df1[df1.iloc[:, 0] == mudaku].copy()
    selected_mudakku_df = make_links_clickable(selected_mudakku_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
    st.markdown(selected_mudakku_df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Namayogam section
    st.markdown("<h2 style='text-align: center; color: black;'>நாம யோக பலன்கள்</h2>", unsafe_allow_html=True)
    df2 = pd.read_excel("Namayoga Palankal.xlsx", engine="openpyxl")
    nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].values)
    selected_namayogam_df = df2[df2.iloc[:, 0] == nam_yogam].copy()
    selected_namayogam_df = make_links_clickable(selected_namayogam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])

    # Split and display the DataFrame sections
    first_part = selected_namayogam_df.iloc[:, :4]
    second_part = selected_namayogam_df.iloc[:, 4:]
    combined_df = pd.concat([selected_namayogam_df.iloc[:, :1], second_part], axis=1)

    st.markdown(first_part.to_html(escape=False, index=False), unsafe_allow_html=True)
    st.markdown(combined_df.to_html(escape=False, index=False), unsafe_allow_html=True)
