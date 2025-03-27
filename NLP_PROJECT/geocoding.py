from geopy.geocoders import Nominatim
import time
import pandas as pd
# Initialize geolocator
geolocator = Nominatim(user_agent="traffic_mapper")
input_file_path = 'Traffic_Data_With_Alerts.csv'  # Replace with the correct path to your dataset
traffic_data = pd.read_csv(input_file_path)
# Function to fetch coordinates
def get_coordinates(location):
    try:
        if pd.isnull(location):
            return None, None
        geocode = geolocator.geocode(location)
        time.sleep(1)  # To avoid exceeding the rate limit
        return (geocode.latitude, geocode.longitude) if geocode else (None, None)
    except:
        return (None, None)

# Apply geocoding to the Traffic_Location column
traffic_data[['Latitude', 'Longitude']] = traffic_data['Traffic_Location'].apply(get_coordinates).apply(pd.Series)

# Save the updated dataset
traffic_data.to_csv('Traffic_Data_With_Coordinates.csv', index=False)
print("Geocoded locations saved to 'Traffic_Data_With_Coordinates.csv'.")
