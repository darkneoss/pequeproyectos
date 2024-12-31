import os
import pandas as pd
import requests
from glob import glob
from tqdm import tqdm
import time
import sys

# Cambiar el directorio de trabajo al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

GOOGLE_MAPS_API_KEY = 'TU API AQUI'

def obtener_coordenadas(direccion):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={direccion}&key={GOOGLE_MAPS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"No se encontraron coordenadas para la dirección: {direccion}")
        return None, None

def generar_kml(df, output_dir):
    kml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    kml_content += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    kml_content += '  <Document>\n'
    for _, row in df.iterrows():
        if pd.notnull(row['Latitud']) and pd.notnull(row['Longitud']):
            kml_content += '    <Placemark>\n'
            kml_content += f'      <name>{row["direccion"]}</name>\n'
            kml_content += '      <Point>\n'
            kml_content += f'        <coordinates>{row["Longitud"]},{row["Latitud"]},0</coordinates>\n'
            kml_content += '      </Point>\n'
            kml_content += '    </Placemark>\n'
    kml_content += '  </Document>\n'
    kml_content += '</kml>\n'
    
    kml_filename = os.path.join(output_dir, 'output_geocodificado.kml')
    with open(kml_filename, 'w', encoding='utf-8') as f:
        f.write(kml_content)
    
    print(f"Archivo KML guardado en: {kml_filename}")

def procesar_excel():
    # Busca un archivo Excel en el directorio actual
    input_files = glob("*.xlsx")
    
    if len(input_files) == 0:
        print("Error: No se encontró ningún archivo Excel en el directorio.")
        return
    elif len(input_files) > 1:
        print("Error: Hay más de un archivo Excel en el directorio. Solo debe haber uno.")
        return
    
    input_filename = input_files[0]
    df = pd.read_excel(input_filename)
    
    if 'direccion' not in df.columns:
        print("Error: La columna 'direccion' no se encontró en el archivo.")
        return
    
    latitudes = []
    longitudes = []
    
    # Utilizar tqdm para mostrar la barra de progreso
    for direccion in tqdm(df['direccion'], desc="Obteniendo coordenadas", unit="dir"):
        lat, lng = obtener_coordenadas(direccion)
        latitudes.append(lat)
        longitudes.append(lng)
        # Agrega una pausa de 0.5 segundos entre cada solicitud
        time.sleep(0.5)
    
    df['Latitud'] = latitudes
    df['Longitud'] = longitudes
    
    output_dir = os.path.join(os.path.dirname(input_filename), 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    output_filename = os.path.join(output_dir, 'output_geocodificado.xlsx')
    df.to_excel(output_filename, index=False)
    print(f"Archivo guardado en: {output_filename}")
    
    # Generar archivo KML
    generar_kml(df, output_dir)

# Ejecuta el procesamiento del archivo de Excel
procesar_excel()

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para cerrar...")
