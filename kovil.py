import streamlit as st
import pandas as pd


# Function to make "இணையதள இணைப்பு" column clickable
def make_links_clickable(df, link_column):
    if link_column in df.columns:
        df[link_column] = df[link_column].apply(
            lambda x: f'<a href="{x}" target="_blank">Click here</a>' if pd.notna(x) else '')
    return df


# Header Information
st.markdown(
    "<h1 style='text-align: center; color: black;'>திதி யோக கரண ஆராய்ச்சியாளர் திரு. சந்திர சிவக்குமார்</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: black;'>கால பைரவர் ஜோதிட பவனம் காடையாம்பட்டி சேலம் மாவட்டம்</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: black;'>Cell: +91 8883113734</h1>",
    unsafe_allow_html=True)

# Sidebar selection for Tithi, Yogam, Mudakku, and Karanam
tithi_type = st.sidebar.selectbox("திதி", ('வளர்பிறை திதி', 'தேய்பிறை திதி'))

# Load respective data based on Tithi type
if tithi_type == 'வளர்பிறை திதி':
    df = pd.read_excel("mohan01.xlsx", engine="openpyxl")
    st.markdown("<h1 style='text-align: center; color: black;'>வளர்பிறை திதி</h1>", unsafe_allow_html=True)
else:
    df = pd.read_excel("mohan02.xlsx", engine="openpyxl")
    st.markdown("<h1 style='text-align: center; color: black;'>தேய்பிறை திதி</h1>", unsafe_allow_html=True)

# Tithi selection with clickable link
tithi = st.sidebar.selectbox('திதி', df.iloc[:, 0].values)
selected_tithi_df = df[df.iloc[:, 0] == tithi].copy()

# Make the link clickable
selected_tithi_df = make_links_clickable(selected_tithi_df, 'இணையதள இணைப்பு')
st.markdown(selected_tithi_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Namayogam section with clickable link
st.markdown("<h1 style='text-align: center; color: black;'>நாம யோகங்கள்</h1>", unsafe_allow_html=True)
df2 = pd.read_excel("mohan03.xlsx", engine="openpyxl")
nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].values)
selected_namayogam_df = df2[df2.iloc[:, 0] == nam_yogam].copy()

# Make the link clickable
selected_namayogam_df = make_links_clickable(selected_namayogam_df, 'இணையதள இணைப்பு')
st.markdown(selected_namayogam_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Mudakku section with clickable link
st.markdown("<h1 style='text-align: center; color: black;'>முடக்கு</h1>", unsafe_allow_html=True)
df3 = pd.read_excel("mohan04.xlsx", engine="openpyxl")
mudakku = st.sidebar.selectbox('முடக்கு', df3['முடக்கு பாவகம் '].unique())
mudakku_rasi = st.sidebar.selectbox("முடக்கு ராசி/கிரகம்", df3['முடக்கு ராசி/கிரகம்'].unique())
selected_mudakku_df = df3[(df3['முடக்கு பாவகம் '] == int(mudakku)) & (df3['முடக்கு ராசி/கிரகம்'] == mudakku_rasi)].copy()

# Make the link clickable
selected_mudakku_df = make_links_clickable(selected_mudakku_df, 'இணையதள இணைப்பு')
st.markdown(selected_mudakku_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Vainasikam section with clickable link
st.markdown("<h1 style='text-align: center; color: black;'>வைநாசிகம்</h1>", unsafe_allow_html=True)
df4 = pd.read_excel("mohan05.xlsx", engine="openpyxl")
vainasikam = st.sidebar.selectbox('வைநாசிகம்', df4.iloc[:, 0].values)
selected_vainasikam_df = df4[df4.iloc[:, 0] == vainasikam].copy()

# Make the link clickable
selected_vainasikam_df = make_links_clickable(selected_vainasikam_df, 'இணையதள இணைப்பு')
st.markdown(selected_vainasikam_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Karanam section with clickable link
st.markdown("<h1 style='text-align: center; color: black;'>கரணம்</h1>", unsafe_allow_html=True)
df5 = pd.read_excel("mohan06.xlsx", engine="openpyxl")
karanam = st.sidebar.selectbox('கரணம்', df5.iloc[:, 0].values)
selected_karanam_df = df5[df5.iloc[:, 0] == karanam].copy()

# Make the link clickable
selected_karanam_df = make_links_clickable(selected_karanam_df, 'இணையதள இணைப்பு')
st.markdown(selected_karanam_df.to_html(escape=False, index=False), unsafe_allow_html=True)
