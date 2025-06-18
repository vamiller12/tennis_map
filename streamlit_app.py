import streamlit as st
import folium
from streamlit_folium import st_folium

# Hardcoded location data
locations = [
    {"name": "Location 1", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "Location 2", "latitude": 34.0522, "longitude": -118.2437}
]

# Streamlit app title
st.title('Chicagoland Area Tennis Courts')

# Create a Folium map
m = folium.Map(location=[41.8781, -87.6298], zoom_start=10)

# Add markers to the map
for location in locations:
    folium.Marker(
        [location['latitude'], location['longitude']],
        popup=location['name']
    ).add_to(m)

# Display the map in the Streamlit app
st_folium(m, width=700, height=500)