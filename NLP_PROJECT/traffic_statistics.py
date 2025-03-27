import pandas as pd

# Load the dataset
ner_data = pd.read_csv('Traffic_Data_With_NER.csv')

# Ensure the Named_Entities column is properly formatted as dictionaries
ner_data['Named_Entities'] = ner_data['Named_Entities'].apply(eval)

# Extract landmarks
landmarks = ner_data['Named_Entities'].apply(lambda x: x.get('landmark', None) if isinstance(x, dict) else None)

# 1. Find the most traffic-prone area
most_traffic_prone_area = landmarks.value_counts().idxmax()

# 2. Find the most common traffic cause (if Cause column exists)
if 'Cause' in ner_data.columns:
    most_common_traffic_cause = ner_data['Cause'].value_counts().idxmax()
else:
    most_common_traffic_cause = "Cause information not available in the dataset."

# Display results
print("Most Traffic-Prone Area:", most_traffic_prone_area)
print("Most Common Traffic Cause:", most_common_traffic_cause)
