import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sys

sys.path.append('C:/Users/dell/Documents/Data science/campusX/project/real_state_project/New folder/Streamlit_project/')
from recommend import PropertyRecommender

st.set_page_config(page_title="Flat Recommendation System")

st.title("Flat Recommendation System")

@st.cache_resource
def load_data():
    with open('recommender_df.pkl', 'rb') as file:
        df = pickle.load(file)

    with open('recommend_pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    with open('cosine_sim.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)

    return df, pipeline, cosine_sim


df, pipeline, cosine_sim = load_data()

if "level_1_recommendations" not in st.session_state:
    st.session_state["level_1_recommendations"] = None

if "selected_property" not in st.session_state:
    st.session_state["selected_property"] = None

bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['No_Bedroom'].unique().tolist())))
min_price = float(st.number_input('Minimum Price (in Crs)', min_value=0.0))
max_price = float(st.number_input('Maximum Price (in Crs)', min_value=min_price))

if st.button('Find Recommendations'):
    pipeline.named_steps['recommend'].no_bedrooms = bedrooms
    pipeline.named_steps['recommend'].min_price = min_price
    pipeline.named_steps['recommend'].max_price = max_price
    pipeline.named_steps['recommend'].cosine_sim = cosine_sim

    first_level_recommendations = pipeline.transform(df)

    if 'Message' in first_level_recommendations.columns:
        st.warning(first_level_recommendations['Message'][0])
        st.session_state["level_1_recommendations"] = None
    else:
        st.session_state["level_1_recommendations"] = first_level_recommendations
        st.session_state["selected_property"] = None

if st.session_state["level_1_recommendations"] is not None:
    st.subheader("Level 1 Recommendations")
    st.dataframe(st.session_state["level_1_recommendations"])

    selected_property_index = st.selectbox(
        "Select a Property for Level 2 Recommendations",
        st.session_state["level_1_recommendations"].index,
        format_func=lambda idx: f"Property {idx + 1}"
    )

    st.session_state["selected_property"] = selected_property_index

if st.session_state["selected_property"] is not None:
    selected_idx = st.session_state["selected_property"]

    similarity_scores = list(enumerate(cosine_sim[selected_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    top_similar_indices = [i[0] for i in similarity_scores if i[0] != selected_idx][:5]

    second_level_recommendations = df.iloc[top_similar_indices].copy()
    second_level_recommendations['SimilarityScore'] = [
        similarity_scores[i][1] for i in range(len(top_similar_indices))
    ]
    second_level_recommendations = second_level_recommendations.drop(columns = ['SimilarityScore'])

    st.subheader("Level 2 Recommendations (Similar Properties)")
    st.dataframe(second_level_recommendations)
