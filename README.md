# Real Estate Price Prediction and Recommendation App

Welcome to the **Real Estate Price Prediction and Recommendation App**! This project is a comprehensive solution that enables users to predict property prices, analyze real estate data through visualizations, and get personalized property recommendations. Built using Python, Streamlit, and various machine learning techniques, this project is designed to provide insights and decision support for the real estate market.

---

## **Features**

### 1. **Price Prediction**
- Predict the price of a property based on user inputs such as location, size, amenities, and other property attributes.
- Machine Learning pipeline for accurate predictions.

### 2. **Data Visualization**
- Explore real estate trends through interactive visualizations:
  - Scatter maps of property locations and prices.
  - Pie charts showing property distributions.
  - Word clouds highlighting property features.
  - Scatter plots and box plots for price comparisons.

### 3. **Recommendation System**
- A two-level recommendation system:
  - Level 1: Recommendations based on user-selected criteria like budget and number of bedrooms.
  - Level 2: Recommendations for similar properties based on cosine similarity.

### 4. **Streamlit Web App**
- Intuitive, user-friendly interface to interact with all features.

---

## **Technologies Used**

- **Python**
- **Streamlit** for building the web application.
- **Machine Learning** using Scikit-Learn and Pickle pipelines.
- **Visualization** with Plotly, Matplotlib, and Seaborn.
- **NLP** for feature word cloud generation.

---

## ** Run the Streamlit App**
```bash
streamlit run pages/home.py
```

---

## **Usage**

### **Home Page**
- Overview of the app, its features, and instructions for use.

### **Price Prediction**
1. Enter property details (e.g., size, location, amenities).
2. Click on `Predict` to view the estimated price range.

### **Data Visualization**
- Explore property trends through interactive graphs and charts.

### **Recommendation System**
1. Provide budget and bedroom preferences.
2. View recommended properties.
3. Select a property to get similar recommendations.

---

## **Model Details**

### **Price Prediction**
- **Algorithm**: Gradient Boosting (XGBoost)
- **Target Variable**: Log-transformed property price for better accuracy.
- **Features**:
  - Property size, age, location, amenities, and more.

### **Recommendation System**
- **Approach**: Content-based filtering using cosine similarity.
- **Features**: Number of bedrooms, budget range, property attributes.

---

## **Data Sources**
- Real estate datasets (cleaned and preprocessed).
- Derived features for advanced insights (e.g., price per square foot, luxury categories).

---



Thank you for exploring the Real Estate App! 🚀
