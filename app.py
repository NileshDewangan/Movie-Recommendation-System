import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    '''Function takes movie_id (integer) and returns poster link'''
    api_key = 'c9bd7d6f35fb8240a8bf7ffa6cc24c1b'
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
    
    # sending request to the api
    data = requests.get(url)
    data = data.json()
    
    # getting appropriate data from reasponse data of api
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    
    return full_path

def recommend(movie):
    '''Function takes a movie (string) and returns 6 similar movie names list and 6 movie poster list'''
    index = movies[movies['title'] == movie].index[0]
    top_20 = similarity[index]
    
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in top_20[1:7]:
        
        movie_id = movies.iloc[i].movie_id
        # fetch the movie poster
        poster = fetch_poster(movie_id)
        
        recommended_movie_posters.append(poster)
        recommended_movie_names.append(movies.iloc[i].title)

    return recommended_movie_names, recommended_movie_posters, 


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

