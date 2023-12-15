import streamlit as st
import pandas as pd
import base64
from PIL import Image
col1, col2= st.columns(2)
with col1:
   st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
   image = Image.open("image.jpg")
   new_image = image.resize((200, 250))
   st.image(new_image)
with col2:
   
   st.markdown("**<h1 style='text-align: center; color: black;'>திரு சிவக்குமார் திதி யோக கரண ஆராய்ச்சியாளர்</h1>**", unsafe_allow_html=True)
   #st.header("திரு சிவக்குமார் திதி யோக கரண ஆராய்ச்சியாளர் ")
   st.markdown("***<h1 style='text-align: center; color: black;'>கால பைரவர் ஜோதிட பவனம் காடையாம்பட்டி சேலம்</h1>***", unsafe_allow_html=True)
   #st.write("**கால பைரவர் ஜோதிட பவனம் காடையாம்பட்டி சேலம்**")
   st.markdown("***<h1 style='text-align: center; color: black;'>cell: +91 8883113734, +91 6379411673</h1>***", unsafe_allow_html=True)
   #st.write("**cell: +91 8883113734, +91 6379411673**")


#st.image("image.jpg",width=400,use_column_width=200)
# Define the filedownload function
#def filedownload(df):
    #csv = df.to_csv(index=False)
    #b64 = base64.b64encode(csv.encode()).decode()  # encoding the data
    #href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
    #return href
h=st.sidebar.selectbox("திதி",('வளர்பிறை திதி','தேய்பிறை திதி'))
# Your code to read the Excel file
if h=='வளர்பிறை திதி':
    st.markdown("**<h1 style='text-align: center; color: black;'>வளர்பிறை திதி</h1>**", unsafe_allow_html=True)
    #st.subheader('வளர்பிறை திதி')
    df = pd.read_excel("mohan01.xlsx", engine="openpyxl")
    #st.table(df)
    a=st.sidebar.selectbox(
    'வளர்பிறை திதி',
    ('பிரதமை', 'துவிதியை', 'திருதியை',"சதுர்த்தி","பஞ்சமி","சஷ்டி","சப்தமி","அஷ்டமி","நவமி","தசமி",
     "ஏகாதசி","துவாதசி","திரயோதசி","சதுர்த்தசி","பவுர்ணமி"))
    if a=='பிரதமை':
        s=st.table(df.iloc[0].reset_index())
    elif a=='துவிதியை':
        s=st.table(df.iloc[1])
    elif a=='திருதியை':
        s=st.table(df.iloc[2])
    elif a=='சதுர்த்தி':
        s=st.table(df.iloc[3])
    elif a=='பஞ்சமி':
        s=st.table(df.iloc[4])
    elif a=='சஷ்டி':
        s=st.table(df.iloc[5])
    elif a=='சப்தமி':
        s=st.table(df.iloc[6])
    elif a=='அஷ்டமி':
        s=st.table(df.iloc[7])
    elif a=='நவமி':
        s=st.table(df.iloc[8])
    elif a=='தசமி':
        s=st.table(df.iloc[9])
    elif a=='ஏகாதசி':
        st.table(df.iloc[10])
    elif a=='துவாதசி':
        s=st.table(df.iloc[11])
    elif a=='திரயோதசி':
        s=st.table(df.iloc[12])
    elif a=='சதுர்த்தசி':
        s=st.table(df.iloc[13])
    elif a=='பவுர்ணமி':
        s=st.table(df.iloc[14])
else:
    st.markdown("**<h1 style='text-align: center; color: black;'>தேய்பிறை திதி</h1>**", unsafe_allow_html=True)
    #st.header('தேய்பிறை திதி')
    df1 = pd.read_excel("mohan02.xlsx", engine="openpyxl")
    #st.table(df1)
    b=st.sidebar.selectbox(
    'தேய்பிறை திதி',
        ('பிரதமை', 'துவிதியை', 'திருதியை',"சதுர்த்தி","பஞ்சமி","சஷ்டி","சப்தமி","அஷ்டமி","நவமி","தசமி",
        "ஏகாதசி","துவாதசி","திரயோதசி","சதுர்த்தசி","அமாவாசை"))
    if b=='பிரதமை':
        t=st.table(df1.iloc[0].reset_index())
    elif b=='துவிதியை':
        t=st.table(df1.iloc[1])
    elif b=='திருதியை':
        t=st.table(df1.iloc[2])
    elif b=='சதுர்த்தி':
        t=st.table(df1.iloc[3])
    elif b=='பஞ்சமி':
        t=st.table(df1.iloc[4])
    elif b=='சஷ்டி':
        t=st.table(df1.iloc[5])
    elif b=='சப்தமி':
        t=st.table(df1.iloc[6])
    elif b=='அஷ்டமி':
        t=st.table(df1.iloc[7])
    elif b=='நவமி':
        t=st.table(df1.iloc[8])
    elif b=='தசமி':
        t=st.table(df1.iloc[9])
    elif b=='ஏகாதசி':
        t=st.table(df1.iloc[10])
    elif b=='துவாதசி':
        t=st.table(df1.iloc[11])
    elif b=='திரயோதசி':
        t=st.table(df1.iloc[12])
    elif b=='சதுர்த்தசி':
        t=st.table(df1.iloc[13])
    elif b=='அமாவாசை':
        t=st.table(df1.iloc[14])
st.markdown("**<h1 style='text-align: center; color: black;'>நாம யோகங்கள்</h1>**", unsafe_allow_html=True)
#st.subheader('நாம யோகங்கள்')
df2 = pd.read_excel("mohan03.xlsx", engine="openpyxl")
#st.table(df2)
c=st.sidebar.selectbox( 'நாம யோகங்கள்',
    ('விஷ்கம்பம்', 'ப்ரீதி',"ஆயுஷ்மான்","சவுபாக்கியம்","சோபனம்","அதிகண்டம்","சுகர்மம்","திருதி","சூலம்",
     "கண்டம்","விருத்தி","துருவம்","வியாகாதம்","அரிசனம்","வச்சிரம்","சித்தி","வியதீபாதம்","வரியான்","பரிகம்",
     "சிவம்","சித்தம்","சாத்தியம்","சுபம்","சுப்பிரம்","பிராம்மம்","மாஹேத்திரம்","வைத்திருதி"))
if c=='விஷ்கம்பம்':
    u=st.table(df2.iloc[0])
elif c=='ப்ரீதி':
    u=st.table(df2.iloc[1])
elif c=='ஆயுஷ்மான்':
    u=st.table(df2.iloc[2])
elif c=='சவுபாக்கியம்':
    u=st.table(df2.iloc[3])
elif c=='சோபனம்':
    u=st.table(df2.iloc[4])
elif c=='அதிகண்டம்':
    u=st.table(df2.iloc[5])
elif c=='சுகர்மம்':
    u=st.table(df2.iloc[6])
elif c=='திருதி':
    u=st.table(df2.iloc[7])
elif c=='சூலம்':
    u=st.table(df2.iloc[8])
elif c=='கண்டம்':
    u=st.table(df2.iloc[9])
elif c=='விருத்தி':
    u=st.table(df2.iloc[10])
elif c=='துருவம்':
    u=st.table(df2.iloc[11])
elif c=='வியாகாதம்':
    u=st.table(df2.iloc[12])
elif c=='அரிசனம்':
    u=st.table(df2.iloc[13])
elif c=='வச்சிரம்':
    u=st.table(df2.iloc[14])
elif c=='சித்தி':
    u=st.table(df2.iloc[15])
elif c=='வியதீபாதம்':
    u=st.table(df2.iloc[16])
elif c=='வரியான்':
    u=st.table(df2.iloc[17])
elif c=='பரிகம்':
    u=st.table(df2.iloc[18])
elif c=='சிவம்':
    u=st.table(df2.iloc[19])
elif c=='சித்தம்':
    u=st.table(df2.iloc[20])
elif c=='சாத்தியம்':
    u=st.table(df2.iloc[21])
elif c=='சுபம்':
    u=st.table(df2.iloc[22])
elif c=='சுப்பிரம்':
    u=st.table(df2.iloc[23])
elif c=='பிராம்மம்':
    u=st.table(df2.iloc[24])
elif c=='மாஹேத்திரம்':
    su=t.table(df2.iloc[25])
elif c=='வைத்திருதி':
    u=st.table(df2.iloc[26])
st.markdown("**<h1 style='text-align: center; color: black;'>முடக்கு</h1>**", unsafe_allow_html=True)
#st.subheader('முடக்கு')
df3 = pd.read_excel("mohan04.xlsx", engine="openpyxl")
#st.table(df3)
d=st.sidebar.selectbox( 'முடக்கு',
    ('1', '2',"3","4","5","6","7","8","9","10","11","12"))
e=st.sidebar.selectbox("முடக்கு ராசி/கிரகம்",("முதல் ராசி","ராகு","கேது","மேஷம் /விருச்சிகமாக அமைந்தால்",
                                              "ரிஷபம் / துலாமாக அமைந்தால்","மிதுனம் / கன்னியாக அமைந்தால்",
                                              "கடகமாக அமைந்தால்","சிம்மமாக அமைந்தால்","தனுசு /மீனமாக அமைந்தால்",
                                              "மகரம் / கும்பமாக அமைந்தால்","ராகு இருந்தால்","கேது இருந்தால்"))
if d=="1":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==1])
    y=df3[df3['முடக்கு பாவகம் ']==1]
    if e=="முதல் ராசி":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="முதல் ராசி"])
    elif e=="ராகு":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு"])
    elif e=="கேது":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது"])
elif d=="2":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==2])
    y=df3[df3['முடக்கு பாவகம் ']==2]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="3":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==3])
    y=df3[df3['முடக்கு பாவகம் ']==3]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="4":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==4])
    y=df3[df3['முடக்கு பாவகம் ']==4]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="5":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==5])
    y=df3[df3['முடக்கு பாவகம் ']==5]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="6":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==6])
    y=df3[df3['முடக்கு பாவகம் ']==6]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="7":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==7])
    y=df3[df3['முடக்கு பாவகம் ']==7]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="8":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==8])
    y=df3[df3['முடக்கு பாவகம் ']==8]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="9":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==9])
    y=df3[df3['முடக்கு பாவகம் ']==9]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="10":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==10])
    y=df3[df3['முடக்கு பாவகம் ']==10]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="11":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==11])
    y=df3[df3['முடக்கு பாவகம் ']==11]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
elif d=="12":
    #x=st.table(df3[df3['முடக்கு பாவகம் ']==12])
    y=df3[df3['முடக்கு பாவகம் ']==12]
    if e=="மேஷம் /விருச்சிகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மேஷம் /விருச்சிகமாக அமைந்தால்"])
    elif e=="ரிஷபம் / துலாமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ரிஷபம் / துலாமாக அமைந்தால்"])
    elif e=="மிதுனம் / கன்னியாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மிதுனம் / கன்னியாக அமைந்தால்"])
    elif e=="கடகமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கடகமாக அமைந்தால்"])
    elif e=="சிம்மமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="சிம்மமாக அமைந்தால்"])
    elif e=="தனுசு /மீனமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="தனுசு /மீனமாக அமைந்தால்"])
    elif e=="மகரம் / கும்பமாக அமைந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="மகரம் / கும்பமாக அமைந்தால்"])
    elif e=="ராகு இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="ராகு இருந்தால்"])
    elif e=="கேது இருந்தால்":
        v=st.table(y[y["முடக்கு ராசி/கிரகம்"]=="கேது இருந்தால்"])
st.markdown("**<h1 style='text-align: center; color: black;'>வைநாசிகம்</h1>**", unsafe_allow_html=True)
#st.subheader('வைநாசிகம்')
df4 = pd.read_excel("mohan05.xlsx", engine="openpyxl")
g=st.sidebar.selectbox( 'வைநாசிகம்',
    ('அஸ்வினி', 'பரணி',"கிருத்திகை","ரோகிணி","மிருகஷீரிடம்","திருவாதிரை","புனர்பூசம்","பூசம்","ஆயில்யம்",
     "மகம்","பூரம்","உத்திரம்","அஸ்தம்","சித்திரை","சுவாதி","விசாகம்","அனுஷம்","கேட்டை","மூலம்",
     "பூராடம்","உத்திராடம்","திருவோணம்","அவிட்டம்","சதயம்","பூரட்டாதி","உத்திரட்டாதி","ரேவதி"))
if g=='அஸ்வினி':
    w=st.table(df4.iloc[0])
elif g=='பரணி':
    w=st.table(df4.iloc[1])
elif g=='கிருத்திகை':
    w=st.table(df4.iloc[2])
elif g=='ரோகிணி':
    w=st.table(df4.iloc[3])
elif g=='மிருகஷீரிடம்':
    w=st.table(df4.iloc[4])
elif g=='திருவாதிரை':
    w=st.table(df4.iloc[5])
elif g=='புனர்பூசம்':
    w=st.table(df4.iloc[6])
elif g=='பூசம்':
    w=st.table(df4.iloc[7])
elif g=='ஆயில்யம்':
    w=st.table(df4.iloc[8])
elif g=='மகம்':
    w=st.table(df4.iloc[9])
elif g=='பூரம்':
    w=st.table(df4.iloc[10])
elif g=='உத்திரம்':
    w=st.table(df4.iloc[11])
elif g=='அஸ்தம்':
    w=st.table(df4.iloc[12])
elif g=='சித்திரை':
    w=st.table(df4.iloc[13])
elif g=='சுவாதி':
    w=st.table(df4.iloc[14])
elif g=='விசாகம்':
    w=st.table(df4.iloc[15])
elif g=='அனுஷம்':
    w=st.table(df4.iloc[16])
elif g=='கேட்டை':
    w=st.table(df4.iloc[17])
elif g=='மூலம்':
    w=st.table(df4.iloc[18])
elif g=='பூராடம்':
    w=st.table(df4.iloc[19])
elif g=='உத்திராடம்':
    w=st.table(df4.iloc[20])
elif g=='திருவோணம்':
    w=st.table(df4.iloc[21])
elif g=='அவிட்டம்':
    w=st.table(df4.iloc[22])
elif g=='சதயம்':
    w=st.table(df4.iloc[23])
elif g=='பூரட்டாதி':
    w=st.table(df4.iloc[24])
elif g=='உத்திரட்டாதி':
    w=st.table(df4.iloc[25])
elif g=='ரேவதி':
    w=st.table(df4.iloc[26])
st.markdown("**<h1 style='text-align: center; color: black;'>கரணம்</h1>**", unsafe_allow_html=True)
#st.subheader('கரணம்')
df5 = pd.read_excel("mohan06.xlsx", engine="openpyxl")
i=st.sidebar.selectbox( 'கரணம்',
    ('பவம்', 'பாலவம்',"கௌலவம்","தைதுளை","கரசை","வணிசை","பத்திரை","சகுனி","சதுஸ்பாதம்","நாகவம்","கிம்ஸ்துக்கினம்"))
if i=='பவம்':
    j=st.table(df5.iloc[0])
elif i=='பாலவம்':
    j=st.table(df5.iloc[1])
elif i=='கௌலவம்':
    j=st.table(df5.iloc[2])
elif i=='தைதுளை':
    j=st.table(df5.iloc[3])
elif i=='கரசை':
    j=st.table(df5.iloc[4])
elif i=='வணிசை':
    j=st.table(df5.iloc[5])
elif i=='பத்திரை':
    j=st.table(df5.iloc[6])
elif i=='சகுனி':
    j=st.table(df5.iloc[7])
elif i=='சதுஸ்பாதம்':
    j=st.table(df5.iloc[8])
elif i=='நாகவம்':
    j=st.table(df5.iloc[9])
elif i=='கிம்ஸ்துக்கினம்':
    j=st.table(df5.iloc[10])

