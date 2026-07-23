import joblib



model = joblib.dump("sentiment_model.pkl")
vectorizer = joblib.dump("vectorizer.pkl" )


def predict_sentiment(text):
    # Convert the text into TF-IDF features
    text_tfidf = vectorizer.transform([text])

    # Predict the sentiment label
    prediction = model.predict(text_tfidf)[0]

    # Convert the label number to a readable sentiment
    labels = {
        0: "negative",
        1: "neutral",
        2: "positive"
    }

    return labels[prediction]
