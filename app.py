import streamlit as st
import pandas as pd
import numpy as np

import requests

import pickle

df=pickle.load(open('movie_list.pkl','rb'))
similarity_score=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_user):
    movie_index = df[df.title == movie_user].index.values[0]

    similar_movies = pd.DataFrame(enumerate(similarity_score[movie_index])).drop(0, axis='columns').sort_values(by=1, ascending=False)
    similar_movies['Names'] = list(map(lambda x: str(np.squeeze(df[df.index == x]['title'].values)), similar_movies.index.values))
    similar_movies['id'] = list(map(lambda x: int(np.squeeze(df[df.index == x]['id'].values)), similar_movies.index.values))

    recommended_movie_posters = []
    for i in range(13):
        id=similar_movies.id.values[i]
        # Fetch movie poster from the TMDB Database
        recommended_movie_posters.append(fetch_poster(id))

    return similar_movies.Names.values[:13],recommended_movie_posters


selected_movie = st.selectbox(
'Type or select a movie from the dropdown',
(list(df.title.values)))
def get_movie_details(title):
    api_key = "bca49c66" 
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_details = response.json()
        return movie_details
    else:
        return None
try:
    if st.button('Show Recommendation'):
        names,poster = recommend(selected_movie)
        for i in range(1,len(names)):
            if ( i % 4 == 1):
                m=get_movie_details(names[i])
                st.markdown(f"<h4 style='color: red;'>{m['Title']}</h4>", unsafe_allow_html=True)

                col1, col2,col4= st.columns([2,9,4])
                col4.image(m['Poster'], width=250)
                if m['Released']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Released:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Released'])
                if m['Genre']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Genre:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Genre'])
                if m['Director']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Director:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Director'])
                if m['Writer']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Writer:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Writer'])
                if m['Actors']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Actors:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Actors'])
                if m['Awards']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Awards:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Awards'])
                if m['imdbRating']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'IMDbRating:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['imdbRating'])
                if m['BoxOffice']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Collection:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['BoxOffice'])
                if m['Production']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Production:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Production'])
                if m['Plot']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'About:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Plot'])
                st.divider()
            elif (i % 4 == 2):
                m=get_movie_details(names[i])
                st.markdown(f"<h4 style='color: red;'>{m['Title']}</h4>", unsafe_allow_html=True)

                col1, col2,col4= st.columns([2,9,4])
                col4.image(m['Poster'], width=250)
                if m['Released']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Released:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Released'])
                if m['Genre']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Genre:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Genre'])
                if m['Director']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Director:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Director'])
                if m['Writer']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Writer:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Writer'])
                if m['Actors']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Actors:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Actors'])
                if m['Awards']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Awards:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Awards'])
                if m['imdbRating']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'IMDbRating:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['imdbRating'])
                if m['BoxOffice']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Collection:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['BoxOffice'])
                if m['Production']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Production:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Production'])
                if m['Plot']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'About:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Plot'])
                st.divider()
            elif (i % 4 == 3):
                m=get_movie_details(names[i])
                st.markdown(f"<h4 style='color: red;'>{m['Title']}</h4>", unsafe_allow_html=True)

                col1, col2,col4= st.columns([2,9,4])
                col4.image(m['Poster'], width=250)
                if m['Released']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Released:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Released'])
                if m['Genre']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Genre:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Genre'])
                if m['Director']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Director:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Director'])
                if m['Writer']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Writer:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Writer'])
                if m['Actors']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Actors:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Actors'])
                if m['Awards']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Awards:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Awards'])
                if m['imdbRating']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'IMDbRating:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['imdbRating'])
                if m['BoxOffice']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Collection:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['BoxOffice'])
                if m['Production']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Production:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Production'])
                if m['Plot']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'About:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Plot'])
                st.divider()
            elif (i % 4 == 0):
                m=get_movie_details(names[i])
                st.markdown(f"<h4 style='color: red;'>{m['Title']}</h4>", unsafe_allow_html=True)

                col1, col2,col4= st.columns([2,9,4])
                col4.image(m['Poster'], width=250)
                if m['Released']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Released:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Released'])
                if m['Genre']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Genre:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Genre'])
                if m['Director']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Director:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Director'])
                if m['Writer']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Writer:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Writer'])
                if m['Actors']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Actors:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Actors'])
                if m['Awards']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Awards:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Awards'])
                if m['imdbRating']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'IMDbRating:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['imdbRating'])
                if m['BoxOffice']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Collection:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['BoxOffice'])
                if m['Production']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'Production:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Production'])
                if m['Plot']!='N/A':
                    with col1:
                        st.markdown(f"<p style='color:red;'>{'About:  '}</p>", unsafe_allow_html=True)
                    col2.write(m['Plot'])
                st.divider()
except Exception as e:
    pass