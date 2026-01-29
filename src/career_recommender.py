from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_career(user_text, df):
    """
    Recommend the best matching career based on user skills and interests.
    
    Args:
        user_text (str): User skills + interest combined
        df (pd.DataFrame): Dataset with 'skills', 'interest', 'career' columns
    
    Returns:
        str: Recommended career
    """
    # Combine skills + interest in dataset
    df["combined"] = df["skills"] + " " + df["interest"]
    
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["combined"])
    user_vector = vectorizer.transform([user_text])
    
    # Cosine similarity
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)
    
    # Best match
    best_match_index = similarity_scores.argmax()
    recommended_career = df.iloc[best_match_index]["career"]
    
    return recommended_career
