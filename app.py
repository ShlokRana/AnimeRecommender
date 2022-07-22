import streamlit as st
import pickle
import pandas as pd
import requests

anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Anime Recommender')
selected_anime_name = st.selectbox("Select Anime", anime['animename'].values)

# Creating a function for recommend
def recommend(x):
    anime_index = anime[anime['animename'] == x].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda y: y[1])[1:11]

    recommended_anime = []
    for i in anime_list:
        recommended_anime.append(anime.iloc[i[0]].animename)
    return recommended_anime


if st.button('Recommend'):
    predictions = recommend(selected_anime_name)

    for i in predictions:
        st.write(i)