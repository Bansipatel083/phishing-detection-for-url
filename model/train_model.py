import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load dataset
data = pd.read_csv('C:/Users/DELL/Desktop/phishing/data/phishing_dataset.csv')  # Replace with your dataset path
X = data['url']
y = data['label']

# Define the pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert URLs to feature vectors
    ('nb', MultinomialNB())        # Naive Bayes classifier
])

# Train the model
pipeline.fit(X, y)

# Save the pipeline
joblib.dump(pipeline, 'C:/Users/DELL/Desktop/phishing/phishing_model.pkl')
print("Model trained and saved as 'phishing_pipeline.pkl'")
