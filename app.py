import streamlit as st
import pickle
import string
import nltk.data
nltk.data.path.append('./nltk_data')
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Loading vectorizer and model
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    st.write("Vectorizer loaded successfully.")
except Exception as e:
    st.error(f"Error loading vectorizer: {e}")

try:
    model = pickle.load(open('model.pkl', 'rb'))
    st.write("Model loaded successfully.")
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    try:
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
    except Exception as e:
        st.error(f"Error during prediction: {e}")