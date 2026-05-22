import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("skills_dataset.csv")

st.title(" AI Tech Stack Recommender")

st.write("Enter your skills/interests:")

user_input = st.text_input("Example: Python SQL Machine Learning")

if user_input:

    # Combine user input with dataset
    skill_data = df["Skills"].tolist()
    skill_data.append(user_input)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(skill_data)

    # Cosine Similarity
    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    # Get best matches
    scores = similarity.flatten()

    df["Score"] = scores

    recommendations = df.sort_values(by="Score", ascending=False)

    st.subheader("Recommended Roles")

    for i in range(3):
        st.write(f"✅ {recommendations.iloc[i]['Role']}")