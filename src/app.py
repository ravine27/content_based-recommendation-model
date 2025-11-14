import pickle 
import streamlit as st
import requests 

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZDUxOGFhYWM3ZTQ2ZjA0YmUyOTM1NDcyNjRmYmE2ZSIsIm5iZiI6MTc2MjQ1MzMwNS4xMjksInN1YiI6IjY5MGNlNzM5NjkwN2EyMzllNjRjNmU3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0Wbj_7gXOn3SGZpq2aeu2L7SbQ-XeyRwQjUPHioRdFM"
    }
    
    response = requests.get(url, headers=headers)
    movie_data = response.json()
    poster_path= movie_data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie ].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse= True, key= lambda x:x[1])
    recommended_movie_name = []
    recommended_movie_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_name.append(movies.iloc[i[0]].title)
    return recommended_movie_name, recommended_movie_poster

st.header("Movie Recommender System Using Machine Learning")
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movies_list = movies['title'].values
selected_movie = st.selectbox(
    'type or select a movie to get recommendation',
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movies_names, recommended_movies_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_posters[4])
