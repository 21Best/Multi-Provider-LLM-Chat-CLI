from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Load the TweetEval sentiment dataset
dataset = load_dataset("cardiffnlp/tweet_eval", "sentiment")
train_df = dataset["train"].to_pandas()
x = train_df["text"]
y = train_df["label"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y, test_size=0.2,
    random_state=42
)


vectorizer = TfidfVectorizer()
# contains the numerical representation of all the training text
x_train_tfidf = vectorizer.fit_transform(x_train)
x_test_tfidf = vectorizer.transform(x_test)

# create the logistic regression model
model = LogisticRegression(max_iter = 1000)
model.fit(x_train_tfidf, y_train)

y_pred = model.predict(x_test_tfidf)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))







