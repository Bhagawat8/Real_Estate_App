# recommender.py

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class PropertyRecommender(BaseEstimator, TransformerMixin):
    def __init__(self, no_bedrooms=None, min_price=None, max_price=None, cosine_sim=None):
        self.no_bedrooms = no_bedrooms
        self.min_price = min_price
        self.max_price = max_price
        self.cosine_sim = cosine_sim

    def transform(self, X):
        if self.no_bedrooms is None or self.min_price is None or self.max_price is None or self.cosine_sim is None:
            raise ValueError("All inputs (no_bedrooms, min_price, max_price, cosine_sim) must be provided.")

        filtered_df = X[(X['No_Bedroom'] == self.no_bedrooms) & 
                        (X['Price_in_Crore'] >= self.min_price) & 
                        (X['Price_in_Crore'] <= self.max_price)]
        
        if filtered_df.empty:
            return pd.DataFrame({'Message': ['No properties found matching the criteria']})

        filtered_indices = filtered_df.index.tolist()
        filtered_cosine_sim = self.cosine_sim[np.ix_(filtered_indices, filtered_indices)]

        query_idx = 0
        sim_scores = list(enumerate(filtered_cosine_sim[query_idx]))
        sim_scores = [(idx, score) for idx, score in sim_scores if 0 < score < 1]
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        if not sim_scores:
            return pd.DataFrame({'Message': ['No similar properties found with score < 1']})

        similar_property_indices = [filtered_indices[i[0]] for i in sim_scores]
        recommendations_df = X.iloc[similar_property_indices].copy()
        recommendations_df['SimilarityScore'] = [score[1] for score in sim_scores]
        recommendations_df = recommendations_df.sort_values(by=['SimilarityScore'], ascending=False)[:5]
        recommendations_df = recommendations_df.drop(columns=['SimilarityScore'])

        return recommendations_df
