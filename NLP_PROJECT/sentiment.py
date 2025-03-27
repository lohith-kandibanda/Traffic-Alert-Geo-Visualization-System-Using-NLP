from textblob import TextBlob
import pandas as pd


input_file_path = 'Processed_Traffic_Data.csv'  # Ensure this is the file with both 'Traffic_Location' and 'Traffic_Cause'
traffic_data = pd.read_csv(input_file_path)
# Function to compute sentiment
def compute_sentiment(post):
    analysis = TextBlob(post)
    sentiment = analysis.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
    if sentiment > 0:
        return 'Positive'
    elif sentiment == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis
traffic_data['Sentiment'] = traffic_data['Post'].apply(compute_sentiment)

# Save the updated dataset
traffic_data.to_csv('Traffic_Data_With_Sentiment.csv', index=False)
print("Sentiment analysis completed. Results saved to 'Traffic_Data_With_Sentiment.csv'.")
