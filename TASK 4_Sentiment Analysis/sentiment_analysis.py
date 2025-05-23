# Import libraries
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with quotechar to handle commas in reviews
df = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\CODE ALPHA\TASK 4_Sentiment Analysis\reviews.csv", quotechar='"')

# Function to get sentiment
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# View the results
print(df)

# Visualize the sentiment distribution
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
