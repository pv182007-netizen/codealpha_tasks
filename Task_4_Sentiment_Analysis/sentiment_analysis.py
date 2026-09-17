
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

df = pd.read_csv("reviews.csv")

# Simple lexicon-based sentiment analysis
positive_words = {
    "excellent","useful","easy","happy","great","perfectly","amazing",
    "love","good","quality","fine","acceptable"
}
negative_words = {
    "disappointing","stopped","poor","waste","damaged","terrible",
    "uncomfortable","bad","not","high","late"
}

def predict_sentiment(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    pos = sum(word in positive_words for word in words)
    neg = sum(word in negative_words for word in words)
    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    return "Neutral"

df["Predicted_Sentiment"] = df["Review"].apply(predict_sentiment)

print(df[["Review","Predicted_Sentiment"]])
print("\nSentiment counts:")
print(df["Predicted_Sentiment"].value_counts())

df["Predicted_Sentiment"].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()
