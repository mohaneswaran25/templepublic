import streamlit as st
import pandas as pd

# Function to make "இணையதள இணைப்பு" and "இணையதள இணைப்பு.1" columns clickable,
# even if the value is empty or None
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
        width: auto%;
    }
    th, td {
        text-align: center !important;
        vertical-align: middle !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header Information
st.markdown(
    "<h2 style='text-align: center; color: black;'>திதி யோக கரண ஆராய்ச்சியாளர் <br>கால கணித ஜோதிடர்<br> சந்திர சிவக்குமார்<br>கால பைரவர் ஜோதிட பவனம்<br>காடையாம்பட்டி வட்டம் <br> சேலம் மாவட்டம்</h2><h3 style='text-align: center; color: black;'>Cell: +91 8883113734</h3>",
    unsafe_allow_html=True)

# Add text input for the user's name
user_name = st.sidebar.text_input("Enter your name:")

# Display the entered name in the main section
if user_name:
    st.markdown(f"<h3 style='text-align: center; color: black;'>ஜாதகர், {user_name}, வழிபடவேண்டிய கோவில்கள்!</h3>", unsafe_allow_html=True)


# Sidebar selection for Tithi, Yogam, Mudakku, and Karanam
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

# Make both link columns clickable
selected_tithi_df = make_links_clickable(selected_tithi_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Namayogam section with clickable link
st.markdown("<h2 style='text-align: center; color: black;'>நாம யோகங்கள்</h2>", unsafe_allow_html=True)
df2 = pd.read_excel("mohan03.xlsx", engine="openpyxl")
nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].values)
selected_namayogam_df = df2[df2.iloc[:, 0] == nam_yogam].copy()

# Make both link columns clickable
selected_namayogam_df = make_links_clickable(selected_namayogam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])

# Split the DataFrame at the 5th index
first_part = selected_namayogam_df.iloc[:, :5]
second_part = selected_namayogam_df.iloc[:, 5:]


# Concatenate the values from the first part into the second part
# Here, we concatenate row-wise using 'pd.concat'.
combined_df = pd.concat([selected_namayogam_df.iloc[:, :1], second_part], axis=1)

# Display the first part and second part of the DataFrame separately
#st.markdown("<h2>First Part</h2>", unsafe_allow_html=True)
st.markdown(first_part.to_html(escape=False, index=False), unsafe_allow_html=True)

#st.markdown("<h2>Second Part (After Adding First Part)</h2>", unsafe_allow_html=True)
st.markdown(combined_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Mudakku section with clickable link
st.markdown("<h2 style='text-align: center; color: black;'>முடக்கு</h2>", unsafe_allow_html=True)
df3 = pd.read_excel("mohan04.xlsx", engine="openpyxl")
mudakku = st.sidebar.selectbox('முடக்கு', df3['முடக்கு பாவகம் '].unique())
mudakku_rasi = st.sidebar.selectbox("முடக்கு ராசி/கிரகம்", df3['முடக்கு ராசி/கிரகம்'].unique())
selected_mudakku_df = df3[(df3['முடக்கு பாவகம் '] == int(mudakku)) & (df3['முடக்கு ராசி/கிரகம்'] == mudakku_rasi)].copy()

# Make both link columns clickable
selected_mudakku_df = make_links_clickable(selected_mudakku_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
st.markdown(selected_mudakku_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Vainasikam section with clickable link
st.markdown("<h2 style='text-align: center; color: black;'>வைநாசிகம்</h2>", unsafe_allow_html=True)
df4 = pd.read_excel("mohan05.xlsx", engine="openpyxl")
vainasikam = st.sidebar.selectbox('வைநாசிகம்', df4.iloc[:, 0].values)
selected_vainasikam_df = df4[df4.iloc[:, 0] == vainasikam].copy()

# Make both link columns clickable
selected_vainasikam_df = make_links_clickable(selected_vainasikam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
st.markdown(selected_vainasikam_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Karanam section with clickable link
st.markdown("<h2 style='text-align: center; color: black;'>கரணம்</h2>", unsafe_allow_html=True)
df5 = pd.read_excel("mohan06.xlsx", engine="openpyxl")
karanam = st.sidebar.selectbox('கரணம்', df5.iloc[:, 0].values)
selected_karanam_df = df5[df5.iloc[:, 0] == karanam].copy()

# Make both link columns clickable
selected_karanam_df = make_links_clickable(selected_karanam_df, ['இணையதள இணைப்பு', 'இணையதள இணைப்பு.1'])
st.markdown(selected_karanam_df.to_html(escape=False, index=False), unsafe_allow_html=True)
