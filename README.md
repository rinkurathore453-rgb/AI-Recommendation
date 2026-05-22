#  AI Tech Stack Recommender:
This project is an AI based Recommendation System that has been created using the concepts of machine learning, Streamlit, and Python.  
TF-IDF Vectorization and Cosine Similarity are used to recommend suitable Tech Roles according to the skills and interests of the user in the Application.

#  Features:
- Accepts user skills/interests as input
- Leverages AI recommendation logic
- Matches user skills to pre-defined tech roles
- Lists best job recommendations
- Simple and interactive user interface
- Similarity Matching for fast recommendation

#  Technologies Used:
- Python, Streamlit, Pandas, Scikit-learn, TF-IDF Vectorizer, Cosine Similarity

#  AI Concepts Used:

## 1. TF-IDF Vectorization
TFIDF is used to representing text data as numerical vectors according to word importance.

## 2. Cosine Similarity
Cosine similarity compares skills of users to the existing tech-role skills and identifies the top matches.

# 1. Install Required Libraries:
pip install -r requirements.txt
# 2. Run the Application:
streamlit run app.py

# Example Input:
Python SQL Machine Learning
#  Example Output:
- Data Scientist
- AI Engineer
- Backend Developer

# Dataset Used:
The project will employ a custom data set that includes:
 - Tech Roles
   A list of skills that are required for each role.
Example:
| Role | Skills |
Data Scientist | Python based Machine Learning / SQL |
Web Developer | HTML | CSS | JavaScript |
DevOps Engineer (Docker AWS Kubernetes) |

# Future Improvements:
- Use larger datasets
- Add graphical UI enhancements
- Add skill rating system
- Add real-time recommendations
