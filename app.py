import streamlit as st
import pickle
import pandas as pd
import requests



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

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

if st.button('Recommend'):
    recommendations = recommend(option)
    for recommended_movie in recommendations:
        st.write(recommended_movie)