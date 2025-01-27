import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Título de la aplicación
st.title("Parque Azul, Goya")

# Cargar el archivo GeoJSON
geojson_file = "./Parque Azul Goya GJSON.geojson"  # Cambia esto por la ruta de tu archivo GeoJSON
with open(geojson_file, "r") as file:
    geojson_data = json.load(file)

# Crear un mapa de Folium
m = folium.Map(zoom_start=2)  # Zoom inicial bajo para evitar problemas si aún no hay datos

# Definir la función de estilo para el GeoJSON
def style_function(feature):
    return {
        "fillColor": "#001a12",  # Verde oliva oscuro
        "color": "#001a12",     # Borde del mismo color
        "weight": 0.5,            # Grosor del borde
        "fillOpacity": 0.7,     # Opacidad del relleno
    }


# Agregar el GeoJSON al mapa
geo_layer = folium.GeoJson(geojson_data, name="GeoJSON", style_function=style_function)
geo_layer.add_to(m)

# Ajustar las coordenadas automáticamente al GeoJSON
bounds = geo_layer.get_bounds()
m.fit_bounds(bounds)

# Mostrar el mapa en Streamlit
st_data = st_folium(m, width=700, height=500)