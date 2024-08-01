import folium
import os
import random  # Importar el módulo random

# Ruta al directorio que contiene los archivos GeoJSON
geojson_dir = '/home/ketin/EDA-FINAL/peru-geojson-master'

# Crear el mapa centrado en Perú
m = folium.Map(location=[-9.19, -75.0152], zoom_start=6)  # Centrado en Perú

# Función para obtener un color aleatorio
def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Función de estilo para cada entidad
def style_function(feature):
    color = random_color()
    return {
        'fillColor': color,
        'color': color,
        'weight': 1,
        'fillOpacity': 0.6,
    }

# Cargar y añadir las capas de GeoJSON al mapa
def add_geojson_layer(file_name, layer_name, map_obj, is_point=False):
    file_path = os.path.join(geojson_dir, file_name)
    if is_point:
        # Para puntos
        folium.GeoJson(
            file_path,
            name=layer_name,
            marker=folium.Marker(
                icon=folium.Icon(icon='info-sign', color='blue'),  # Ícono más amigable
                popup=folium.Popup(max_width=200)
            )
        ).add_to(map_obj)
    else:
        # Para polígonos
        folium.GeoJson(
            file_path,
            name=layer_name,
            style_function=style_function
        ).add_to(map_obj)

# Añadir capas al mapa
add_geojson_layer('peru_departamental_simple.geojson', 'Departamentos', m)
add_geojson_layer('peru_provincial_simple.geojson', 'Provincias', m)
add_geojson_layer('peru_distrital_simple.geojson', 'Distritos', m)
add_geojson_layer('peru_capital_provincia.geojson', 'Capitales de Provincia', m, is_point=True)

# Añadir un control de capas
folium.LayerControl().add_to(m)

# Guardar el mapa en un archivo HTML
m.save("/home/ketin/EDA-FINAL/peru-mapa-con-capas.html")

