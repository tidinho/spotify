import streamlit as st
import pandas as pd



st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

df = pd.read_csv("Spotify.csv")

st.session_state["df_spotify"] = df

df.set_index("Track", inplace=True)


artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"]== artist]

albuns = df_filtered["Album"].value_counts().index
album = st.sidebar.selectbox("Album", albuns)

df_filtered2 = df[df["Album"]== album]
dysplay = st.checkbox('Dysplay')
if dysplay:
    st.bar_chart(df_filtered2["Stream"])

st.write(artist)

