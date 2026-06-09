import streamlit as st
import pandas as pd

from recommendation import recommend

df = pd.read_csv(
    "data/netflix_titles.csv"
)

st.set_page_config(
    page_title="Netflix Recommender",
    layout="wide"
)

st.title(
    "🎬 Netflix Recommendation System"
)

selected_movie = st.selectbox(
    "Choose a Movie",
    df["title"].values
)

if st.button("Recommend"):

    movies = recommend(
        selected_movie
    )

    st.subheader(
        "Recommended Movies"
    )

    for movie in movies:
        st.write(movie)