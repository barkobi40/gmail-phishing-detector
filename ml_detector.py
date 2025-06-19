import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Initial training (run once to create the model)
def train_model():
    df = pd.read_csv("emails.csv")  # Contains columns: 'text', 'label' (phishing/legit)
    df['label'] = df['label'].map({'phishing': 1, 'legit': 0})

    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', MultinomialNB())
    ])
    pipeline.fit(df['text'], df['label'])
    joblib.dump(pipeline, "phishing_model.pkl")

# Use the model to predict phishing probability
def predict_email(text):
    model = joblib.load("phishing_model.pkl")
    proba = model.predict_proba([text])[0]
    score = round(proba[1] * 10)  # Score between 0 and 10
    return score
