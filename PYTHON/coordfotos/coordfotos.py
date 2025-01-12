import os
import csv
import simplekml
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    """
    Extrae datos EXIF de una imagen.

    Args:
        image (PIL.Image.Image): La imagen de la cual extraer datos EXIF.

    Returns:
        dict: Un diccionario que contiene los datos EXIF.
    """
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            exif_data[tag_name] = value
    return exif_data

def get_gps_info(exif_data):
    """
    Extrae información GPS de los datos EXIF.

    Args:
        exif_data (dict): Un diccionario que contiene datos EXIF.

    Returns:
        dict: Un diccionario que contiene información GPS.
    """
    gps_info = {}
    if "GPSInfo" in exif_data:
        for key in exif_data["GPSInfo"].keys():
            decode = GPSTAGS.get(key, key)
            gps_info[decode] = exif_data["GPSInfo"][key]
    return gps_info

def convert_to_degrees(value):
    """
    Convierte coordenadas GPS almacenadas en grados, minutos y segundos a grados decimales.

    Args:
        value (tuple): Una tupla que contiene las coordenadas GPS en grados, minutos y segundos.

    Returns:
        float: Las coordenadas en grados decimales.
    """
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def get_coordinates(gps_info):
    """
    Extrae latitud y longitud de la información GPS.

    Args:
        gps_info (dict): Un diccionario que contiene información GPS.

    Returns:
        tuple: Una tupla que contiene la latitud y longitud.
    """
    lat = None
    lon = None
    if "GPSLatitude" in gps_info and "GPSLatitudeRef" in gps_info and \
       "GPSLongitude" in gps_info and "GPSLongitudeRef" in gps_info:
        lat = convert_to_degrees(gps_info["GPSLatitude"])
        if gps_info["GPSLatitudeRef"] != "N":
            lat = 0 - lat

        lon = convert_to_degrees(gps_info["GPSLongitude"])
        if gps_info["GPSLongitudeRef"] != "E":
            lon = 0 - lon
    return lat, lon

def extract_coordinates_from_images(directory):
    """
    Extrae coordenadas GPS de todas las imágenes en un directorio.

    Args:
        directory (str): El directorio que contiene las imágenes.

    Returns:
        list: Una lista de tuplas, cada una con el nombre de archivo, latitud y longitud.
    """
    coordinates = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.tiff', '.png')):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            exif_data = get_exif_data(image)
            gps_info = get_gps_info(exif_data)
            lat, lon = get_coordinates(gps_info)
            if lat and lon:
                coordinates.append((filename, lat, lon))
    return coordinates

def save_coordinates_to_csv(coordinates, output_path):
    """
    Guarda coordenadas GPS en un archivo CSV.

    Args:
        coordinates (list): Una lista de tuplas, cada una con el nombre de archivo, latitud y longitud.
        output_path (str): La ruta del archivo CSV de salida.
    """
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for filename, lat, lon in coordinates:
            writer.writerow({'Filename': filename, 'Latitude': lat, 'Longitude': lon})

def save_coordinates_to_kml(coordinates, output_path):
    """
    Guarda coordenadas GPS en un archivo KML.

    Args:
        coordinates (list): Una lista de tuplas, cada una con el nombre de archivo, latitud y longitud.
        output_path (str): La ruta del archivo KML de salida.
    """
    kml = simplekml.Kml()
    
    for filename, lat, lon in coordinates:
        # Crea un punto para cada imagen
        point = kml.newpoint(name=filename)
        point.coords = [(lon, lat)]  # KML usa el orden (longitud, latitud)
        point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/red-circle.png'
        
    kml.save(output_path)

if __name__ == "__main__":
    # Cambia el directorio de trabajo a la ubicación del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Obtiene el directorio actual
    directory = os.getcwd()
    
    print("Extrayendo coordenadas de imágenes...")
    coordinates = extract_coordinates_from_images(directory)
    
    if coordinates:
        # Guardar archivo CSV
        csv_output_path = os.path.join(directory, 'coordinates.csv')
        save_coordinates_to_csv(coordinates, csv_output_path)
        print(f"Coordenadas guardadas en {csv_output_path}")
        
        # Guardar archivo KML
        kml_output_path = os.path.join(directory, 'coordinates.kml')
        save_coordinates_to_kml(coordinates, kml_output_path)
        print(f"Archivo KML guardado en {kml_output_path}")
        
        print(f"\nProcesadas {len(coordinates)} imágenes con coordenadas GPS")
    else:
        print("No se encontraron imágenes con coordenadas GPS en el directorio")
    
    # Esperar entrada del usuario antes de cerrar
    input("\nPresione Enter para salir...")
