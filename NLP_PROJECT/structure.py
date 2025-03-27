import pandas as pd

# Load the dataset with locations and causes
input_file_path = 'Traffic_Data_With_Causes.csv'  # Ensure this is the file with both 'Traffic_Location' and 'Traffic_Cause'
traffic_data = pd.read_csv(input_file_path)

# Combine relevant fields into an alert message
traffic_data['Alert_Message'] = (
    "Traffic alert in " + traffic_data['City'] + " near " +
    traffic_data['Traffic_Location'].fillna('unknown location') +
    ". Cause: " + traffic_data['Traffic_Cause'].fillna('unknown cause') + "."
)

# Save the processed data for further use
processed_file_path = 'Processed_Traffic_Data.csv'  # Adjust path as needed
traffic_data.to_csv(processed_file_path, index=False)

print(f"Final processed traffic data with alert messages has been saved to {processed_file_path}")

# Optional: Display the first few rows in the console for verification
print(traffic_data.head())
