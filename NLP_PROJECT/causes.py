import pandas as pd

# Load the dataset with original posts
input_file_path = 'Traffic_Data_With_Locations.csv'  # Use 'Cleaned_Traffic_Data.csv' if you haven't done location extraction
traffic_data = pd.read_csv(input_file_path)

# Define keywords for causes
cause_keywords = {
    'rain': ['rain', 'waterlogging'],
    'road_construction': ['construction', 'road work'],
    'accident': ['accident', 'crash', 'collision'],
    'vehicle_breakdown': ['breakdown', 'stalled vehicle'],
    'checkpoint': ['police checkpoint', 'security check'],
}

# Function to extract causes
def extract_cause(post):
    for cause, keywords in cause_keywords.items():
        if any(keyword in post.lower() for keyword in keywords):
            return cause
    return 'other'

# Apply cause extraction
traffic_data['Traffic_Cause'] = traffic_data['Post'].apply(extract_cause)

# Save the dataset with extracted causes for further use
output_file_path = 'Traffic_Data_With_Causes.csv'
traffic_data.to_csv(output_file_path, index=False)
print(f"Traffic data with extracted causes has been saved to {output_file_path}")

# Optional: Display the first few rows in the console for verification
print(traffic_data.head())
