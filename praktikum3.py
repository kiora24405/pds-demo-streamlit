import streamlit as st
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[-6.200000, 106.816666], zoom_start=12)
m.save("map.html")
# Title
st.title("Contoh Integrasi Folium + Streamlit")
# Titik peta Indonesia
center_lat = -2.5489
center_lon = 118.0149
# Buat peta Folium
m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
# Tampilkan di Streamlit
st_folium(m, width=700, height=500)