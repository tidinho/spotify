import streamlit as st
import pandas as pd



st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

@st.cache_data
def load_data():
    df = pd.read_csv("Spotify.csv")
    return df

df = load_data()
st.session_state["df_spotify"] = df


df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"]== artist]

albuns = df["Album"].value_counts().index
album = st.sidebar.selectbox('Album', albuns)

df_filtered2 = df[df["Album"]== album]
dysplay = st.checkbox('Dysplay')

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])


st.write(artist)

