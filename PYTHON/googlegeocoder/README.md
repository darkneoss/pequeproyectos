# Geocodificador de Direcciones a KML

Este script de Python permite obtener las coordenadas geográficas (latitud y longitud) a partir de direcciones contenidas en un archivo Excel y genera un archivo KML que puede ser utilizado en aplicaciones como Google Earth.

## Requisitos

- Python 3.x
- Bibliotecas de Python:
  - `pandas`
  - `requests`
  - `tqdm`
  - `openpyxl` (para leer archivos Excel)

Puedes instalar las bibliotecas necesarias utilizando pip:

```bash
pip install pandas requests tqdm openpyxl
```

## Configuración

1. **API de Google Maps**: Necesitarás una clave de API de Google Maps para utilizar el servicio de geocodificación. Puedes obtener una [aquí](https://cloud.google.com/maps-platform/).

2. **Modificar el script**: Abre el script y sustituye `'TU API AQUI'` con tu clave de API de Google Maps:

```python
GOOGLE_MAPS_API_KEY = 'TU API AQUI'
```

## Uso

1. Coloca el script en un directorio junto con un archivo Excel que contenga una columna llamada `direccion`. Este archivo debe tener el formato `.xlsx`.

2. Ejecuta el script desde la terminal:

```bash
python geocodificador.py
```

3. El script buscará un archivo Excel en el directorio actual y procesará las direcciones, generando un nuevo archivo Excel con las coordenadas y un archivo KML en un subdirectorio llamado `processed`.

## Estructura del Archivo Excel

El archivo Excel de entrada debe tener al menos una columna titulada `direccion`, que contiene las direcciones que se desean geocodificar. Por ejemplo:

| direccion                  |
|----------------------------|
| Avenida Siempre Viva 742   |
| Calle Falsa 123            |
| Plaza Mayor                |

## Salida

- Un archivo Excel llamado `output_geocodificado.xlsx` que contiene las direcciones junto con sus respectivas latitudes y longitudes.
- Un archivo KML llamado `output_geocodificado.kml` que puede ser utilizado en Google Earth.

## Notas

- Asegúrate de que solo haya un archivo Excel en el directorio al ejecutar el script. De lo contrario, el script mostrará un mensaje de error.
- El script espera medio segundo entre cada solicitud a la API de Google Maps para evitar sobrepasar los límites de uso.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este script, por favor, abre un issue o un pull request.