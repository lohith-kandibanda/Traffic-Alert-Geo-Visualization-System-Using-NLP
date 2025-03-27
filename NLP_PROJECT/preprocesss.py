import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
file_path = 'Traffic_data.csv'  # Replace with your actual file path
traffic_data = pd.read_csv(file_path)

# Drop unnecessary columns
if 'Unnamed: 0' in traffic_data.columns:
    traffic_data = traffic_data.drop(columns=['Unnamed: 0'])

# Text cleaning function
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    text = ' '.join([word for word in words if word not in stop_words])  # Remove stopwords
    return text

# Apply cleaning
traffic_data['Cleaned_Post'] = traffic_data['Post'].apply(clean_text)

# Save the cleaned data to a CSV file for inspection
output_file_path = 'Cleaned_Traffic_Data.csv'  # Save file to the same directory as the script
traffic_data.to_csv(output_file_path, index=False)
print(f"Cleaned data has been saved to {output_file_path}")

# Optional: Display the first few rows in the console
print(traffic_data.head())
