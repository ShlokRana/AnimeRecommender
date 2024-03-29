import streamlit as st
import bz2file as bz2
import pickle
import pandas as pd
import requests

anime_dict = bz2.BZ2File('anime_dict.pbz2', 'rb')
anime_dict = pickle.load(anime_dict)
anime = pd.DataFrame(anime_dict)
similarity = bz2.BZ2File('similarity.pbz2', 'rb')
similarity = pickle.load(similarity)

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
