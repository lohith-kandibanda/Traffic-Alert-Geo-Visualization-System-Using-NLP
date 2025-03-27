import pandas as pd
import spacy

# Load the dataset
input_file_path = 'Processed_Traffic_Data.csv'  # Replace with the correct path to your dataset
traffic_data = pd.read_csv(input_file_path)

# Load spaCy's small English model
nlp = spacy.load('en_core_web_sm')

# Function to extract all named entities
def extract_entities(post):
    doc = nlp(post)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    return entities

# Apply NER to extract named entities
traffic_data['Named_Entities'] = traffic_data['Post'].apply(extract_entities)

# Save the dataset with named entities
output_file_path = 'Traffic_Data_With_NER.csv'  # Adjust as needed
traffic_data.to_csv(output_file_path, index=False)
print(f"Named entity recognition completed. Results saved to '{output_file_path}'.")
