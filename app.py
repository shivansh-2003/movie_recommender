import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        Movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(Movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# Load the movie_list.pkl file
movie_list_path = '/Users/shivanshmahajan/Desktop/DataScinece/Machine Learning/Projects/movie_recommender/movie_list.pkl'
movie_list = pickle.load(open(movie_list_path, 'rb'))
movies = pd.DataFrame(movie_list)

# Load the similarity.pkl file
similarity_path = '/Users/shivanshmahajan/Desktop/DataScinece/Machine Learning/Projects/movie_recommender/similarity.pkl'
similarity = pickle.load(open(similarity_path, 'rb'))

st.title("Movie Recommender System")

# Use the movie titles from the DataFrame directly
option = st.selectbox("What movie do you like?", movies['title'].values)

if st.button('Show Recommendation'):

    recommended_movie_names,recommended_movie_posters = recommend(option)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
