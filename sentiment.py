import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Title for the app
st.title("Sentiment Analysis Model")
st.write("Sentiment analysis, also known as opinion mining or emotion artificial intelligence, is a method that uses natural language processing (NLP), text analysis, computational linguistics, and biometrics to identify, extract, quantify, and study affective states and subjective information. It involves analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral.")

# Text input field
user_input = st.text_input("Enter text for analyzing the sentiment:")

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Get the sentiment score
sentiment_score = sia.polarity_scores(user_input)

# Determine the sentiment based on the compound score
if sentiment_score['compound'] >= 0.1:
    sentiment = 'Positive'
elif sentiment_score['compound'] <= -0.1:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'

if st.button("Analyze Text"):
  # Display the input text
  st.write("You entered:", user_input)
  st.write("The sentiment of the text is:", sentiment)
