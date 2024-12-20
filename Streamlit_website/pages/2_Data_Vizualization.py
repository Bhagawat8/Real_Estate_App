import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(page_title="Data Vizualization App")
st.title('Analytics')

df = pd.read_csv("C:/Users/dell/Documents/Data science/campusX/project/real_state_project/New folder/Streamlit_project/data_viz1.csv")

numeric_columns = ['Price_in_Crore', 'price_Per_Sqft_converted', 'Super Built-up Area', 'latitude', 'longitude']

group_df = df.groupby('sector_num')[numeric_columns].mean()

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_Per_Sqft_converted", size='Super Built-up Area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map" , width=1200 , height=700 , hover_name=group_df.index)

st.plotly_chart(fig , use_container_width=True)


st.title('Features wordcloud')
with open('feature_text.pkl', 'rb') as file:
    feature_text = pickle.load(file)

wordcloud = WordCloud(
    width=500, 
    height=500, 
    background_color='white', 
    stopwords=set(['s']), 
    min_font_size=10
).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))


ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")  
plt.tight_layout(pad=0)

st.pyplot(fig)

st.header('Area Vs Price')

fig1 = px.scatter(df, x="Super Built-up Area", y="Price_in_Crore", color="No_Bedroom")

st.plotly_chart(fig1 , use_container_width=True)

st.header('BHK Pie Chart')

sector_options = sorted(df['sector_num'].unique().tolist())
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(df, names='No_Bedroom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(df[df['sector_num'] == selected_sector], names='No_Bedroom')

    st.plotly_chart(fig2, use_container_width=True)


st.header('Side by Side BHK price comparison')

fig3 = px.box(df[df['No_Bedroom'] <= 6], x='No_Bedroom', y='Price_in_Crore', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)

st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(df['Price_in_Crore'])
st.pyplot(fig3)