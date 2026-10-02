import joblib
import nltk
from nltk.corpus import stopwords
import string
import streamlit as st

nltk.download('punkt')
nltk.download('stopwords')

def remove_punc(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(txt):
    new = ""
    for i in txt:
        if not i.isdigit():
            new = new + i
    return new

def remove_emojis(txt):
    new = ""
    for i in txt:
        if i.isascii():
            new += i
    return new

stop_words = stopwords.words('english')

def remove(txt):
    words = txt.split()
    cleaned = []
    for i in words:
        if not i in stop_words:
            cleaned.append(i)
    return ' '.join(cleaned)

def preprocess(text):
    text = text.lower()
    text = remove_punc(text)
    text = remove_numbers(text)
    text = remove_emojis(text)
    text = remove(text)
    return text

model = joblib.load('logistic_regression_model.pkl')
tfidf_vec = joblib.load('tfidf_vectorizer.pkl')

emotion_mapping = ['sadness', 'anger', 'love', 'surprise', 'fear', 'joy']

st.title("Sentimental Analysis")
user_input = st.text_input("Enter text here:")

if st.button("Predict"):
    processed_input = preprocess(user_input)
    vectorized_input = tfidf_vec.transform([processed_input])
    prediction = model.predict(vectorized_input)
    predicted_emotion = emotion_mapping[prediction[0]]
    st.write(f"The predicted emotion is: {predicted_emotion}")