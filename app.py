import pickle
import streamlit as st
import requests
import numpy as np
from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity


# ------------------------------
# TMDB Poster Fetch Function
# ------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


# ------------------------------
# Recommendation Function
# ------------------------------
def recommend(movie):
    # get index
    idx = movies[movies['title'] == movie].index[0]

    # TF-IDF vector of selected movie
    movie_vec = tfidf_matrix[idx]

    # compute similarity ON DEMAND
    distances = cosine_similarity(movie_vec, tfidf_matrix).flatten()

    # sort
    similar_indexes = distances.argsort()[::-1][1:6]

    names = []
    posters = []

    for i in similar_indexes:
        movie_id = movies.iloc[i].movie_id
        names.append(movies.iloc[i].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


# ------------------------------
# LOAD FILES (VERY SMALL)
# ------------------------------
movies = pickle.load(open("movies.pkl", "rb"))
tfidf_vectorizer = pickle.load(open("tfidf__vectorizer.pkl", "rb"))
tfidf_matrix = load_npz("tfidf__matrix.npz")

# ------------------------------
# Streamlit UI
# ------------------------------
st.header("Movie Recommender System (TF-IDF Content Based)")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
