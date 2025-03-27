import pandas as pd

# Load the dataset with sentiment and other processed columns
input_file_path = 'Traffic_Data_With_Sentiment.csv'  # Replace with the actual file path
traffic_data = pd.read_csv(input_file_path)

# Generate alert messages
def generate_alert_message(row):
    location = row['Traffic_Location'] if not pd.isnull(row['Traffic_Location']) else 'unknown location'
    cause = row['Traffic_Cause']
    sentiment = row['Sentiment']
    return f"Traffic alert in {row['City']} near {location}. Cause: {cause}. Severity: {sentiment}."

# Create a severity column
def assign_severity(sentiment):
    if sentiment == 'Negative':
        return 'High'
    elif sentiment == 'Neutral':
        return 'Medium'
    else:
        return 'Low'

# Apply alert message and severity
traffic_data['Alert_Message'] = traffic_data.apply(generate_alert_message, axis=1)
traffic_data['Severity'] = traffic_data['Sentiment'].apply(assign_severity)

# Save the updated dataset
output_file_path = 'Traffic_Data_With_Alerts.csv'  # Adjust as needed
traffic_data.to_csv(output_file_path, index=False)
print(f"Alerts generated and saved to '{output_file_path}'.")
