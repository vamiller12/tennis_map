import streamlit as st
import folium
from streamlit_folium import st_folium

# Hardcoded location data
locations = [
    {"name": "HAMILTON (ALEXANDER)", "latitude": 41.76304673, "longitude": -87.63562215},
    {"name": "HIAWATHA", "latitude": 41.94404507, "longitude": -87.82647101}
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
