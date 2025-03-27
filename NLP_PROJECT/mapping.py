import folium
import pandas as pd

# Load the dataset with coordinates
file_path = 'Traffic_Data_With_Coordinates.csv'
traffic_data = pd.read_csv(file_path)

# Generate maps for each city
for city in traffic_data['City'].unique():
    city_data = traffic_data[traffic_data['City'] == city]

    # Calculate the center for the city map
    if 'Latitude' in city_data.columns and 'Longitude' in city_data.columns:
        center_lat = city_data['Latitude'].mean()
        center_lon = city_data['Longitude'].mean()
    else:
        print(f"City {city} does not have latitude/longitude data, skipping map generation.")
        continue

    # Initialize the map for the city
    city_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add markers for each alert in the city
    for _, row in city_data.iterrows():
        if not pd.isnull(row['Latitude']) and not pd.isnull(row['Longitude']):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Alert_Message'],
                tooltip=row['Severity'],
                icon=folium.Icon(color='red' if row['Severity'] == 'High' else 'orange' if row['Severity'] == 'Medium' else 'green')
            ).add_to(city_map)

    # Save the map to an HTML file named after the city
    city_map.save(f"{city}_Traffic_Alerts_Map.html")
    print(f"Map for {city} saved as '{city}_Traffic_Alerts_Map.html'.")
