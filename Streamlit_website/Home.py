import streamlit as st

# Set page configuration
st.set_page_config(page_title="Real Estate App", page_icon="🏠", layout="wide")

# Page Title
st.title("🏠 Welcome to the Real Estate Price Prediction & Recommendation App")

# Description Section
st.markdown(
    """
    ### About the App
    This app is designed to help users:
    - **Predict real estate prices** based on various features like bedrooms, bathrooms, area, etc.
    - **Analyze trends** through advanced visualizations such as scatter plots, pie charts, and box plots.
    - **Discover ideal properties** using a recommendation engine tailored to your preferences.
    """
)

# Main Features Section
st.markdown("### Features at a Glance")
features = [
    "💡 **Price Prediction**: Enter property details to get an estimated price range.",
    "📊 **Data Visualization**: Gain insights into real estate trends with interactive visualizations.",
    "🔍 **Flat Recommendation**: Find the best property based on your preferences and discover similar listings.",
]
for feature in features:
    st.markdown(feature)

# Navigation Section
st.markdown(
    """
    ### Get Started
    Use the navigation menu on the left to explore:
    - **Price Prediction**: Input property details and get predictions.
    - **Data Visualization**: Analyze market trends and visualize property features.
    - **Flat Recommendations**: Discover properties tailored to your needs.
    """
)

# Add a visually engaging section
st.markdown("---")
st.subheader("🔑 Why Choose This App?")
st.markdown(
    """
    - **Ease of Use**: A clean and intuitive interface.
    - **Advanced Analytics**: Powerful tools for deep insights.
    - **Smart Recommendations**: Leverage machine learning for personalized property suggestions.
    """
)

# # Add a call-to-action with images
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 2, 1])

# with col1:
#     st.image("https://via.placeholder.com/150", caption="Predict Prices", use_column_width=True)

# with col2:
#     st.image("https://via.placeholder.com/300x150", caption="Visualize Data Trends", use_column_width=True)

# with col3:
#     st.image("https://via.placeholder.com/150", caption="Find Your Dream Flat", use_column_width=True)

# Footer Section
st.markdown("---")
st.markdown(
    """
    **Developed by [Bhagawat Karhale]**  
    Start exploring now and make informed real estate decisions!
    """
)
