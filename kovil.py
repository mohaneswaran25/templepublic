import streamlit as st
import pandas as pd


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

# Tithi selection
tithi = st.sidebar.selectbox('திதி', df.iloc[:, 0].values)
st.table(df[df.iloc[:, 0] == tithi])

# Namayogam section
st.markdown("<h1 style='text-align: center; color: black;'>நாம யோகங்கள்</h1>", unsafe_allow_html=True)
df2 = pd.read_excel("mohan03.xlsx", engine="openpyxl")
nam_yogam = st.sidebar.selectbox('நாம யோகங்கள்', df2.iloc[:, 0].values)
st.table(df2[df2.iloc[:, 0] == nam_yogam])

# Mudakku section
st.markdown("<h1 style='text-align: center; color: black;'>முடக்கு</h1>", unsafe_allow_html=True)
df3 = pd.read_excel("mohan04.xlsx", engine="openpyxl")
mudakku = st.sidebar.selectbox('முடக்கு', df3['முடக்கு பாவகம் '].unique())
mudakku_rasi = st.sidebar.selectbox("முடக்கு ராசி/கிரகம்", df3['முடக்கு ராசி/கிரகம்'].unique())
st.table(df3[(df3['முடக்கு பாவகம் '] == int(mudakku)) & (df3['முடக்கு ராசி/கிரகம்'] == mudakku_rasi)])

# Vainasikam section
st.markdown("<h1 style='text-align: center; color: black;'>வைநாசிகம்</h1>", unsafe_allow_html=True)
df4 = pd.read_excel("mohan05.xlsx", engine="openpyxl")
vainasikam = st.sidebar.selectbox('வைநாசிகம்', df4.iloc[:, 0].values)
st.table(df4[df4.iloc[:, 0] == vainasikam])

# Karanam section
st.markdown("<h1 style='text-align: center; color: black;'>கரணம்</h1>", unsafe_allow_html=True)
df5 = pd.read_excel("mohan06.xlsx", engine="openpyxl")
karanam = st.sidebar.selectbox('கரணம்', df5.iloc[:, 0].values)
st.table(df5[df5.iloc[:, 0] == karanam])
