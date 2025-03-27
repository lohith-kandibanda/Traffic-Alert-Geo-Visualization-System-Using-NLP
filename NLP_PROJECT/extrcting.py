import spacy
import pandas as pd

# Load the cleaned dataset
input_file_path = 'Cleaned_Traffic_Data.csv'  # Adjust this to the actual file path if needed
traffic_data = pd.read_csv(input_file_path)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to extract locations
def extract_location(post):
    doc = nlp(post)
    locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE']  # GPE = Geo-Political Entity
    return ', '.join(locations)

# Apply location extraction to the 'Post' column
traffic_data['Traffic_Location'] = traffic_data['Post'].apply(extract_location)

# Save the dataset with extracted locations for further use
output_file_path = 'Traffic_Data_With_Locations.csv'
traffic_data.to_csv(output_file_path, index=False)
print(f"Traffic data with extracted locations has been saved to {output_file_path}")

# Optional: Display the first few rows in the console for verification
print(traffic_data.head())
