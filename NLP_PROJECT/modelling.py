import pandas as pd
from gensim import corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the dataset
input_file_path = 'Processed_Traffic_Data.csv'  # Adjust to the correct path of your dataset
traffic_data = pd.read_csv(input_file_path)

# Preprocess text for topic modeling
def preprocess_for_lda(post):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(post.lower())
    return [word for word in words if word.isalpha() and word not in stop_words]

# Tokenize posts
traffic_data['Tokens'] = traffic_data['Cleaned_Post'].apply(preprocess_for_lda)

# Create a dictionary and corpus for LDA
dictionary = corpora.Dictionary(traffic_data['Tokens'])
corpus = [dictionary.doc2bow(text) for text in traffic_data['Tokens']]

# Fit LDA model
lda_model = LdaModel(corpus=corpus, num_topics=3, id2word=dictionary, passes=10)

# Assign topics to each post
def assign_topic(tokens):
    bow = dictionary.doc2bow(tokens)
    topics = lda_model.get_document_topics(bow)
    return max(topics, key=lambda x: x[1])[0] if topics else None

traffic_data['Topic'] = traffic_data['Tokens'].apply(assign_topic)

# Save the dataset with topics
output_file_path = 'Traffic_Data_With_Topics.csv'  # Adjust path if needed
traffic_data.to_csv(output_file_path, index=False)
print(f"Topic modeling completed. Results saved to '{output_file_path}'.")
