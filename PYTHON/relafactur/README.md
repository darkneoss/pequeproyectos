# Extractor de Datos de Facturas Electrónicas XML

Este script en Python permite extraer información relevante de archivos XML de facturas electrónicas y guardarla en un archivo CSV. Está diseñado para facilitar la gestión y análisis de datos de facturación.

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python: `os`, `xml.etree.ElementTree`, `csv`

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando:

   ```bash
   python --version
   ```

## Uso

2. Coloca tus archivos XML de facturas electrónicas en el mismo directorio donde se encuentra el script.

3. Ejecuta el script:

   ```bash
   python relafactur.py
   ```
   
4. El script procesará todos los archivos XML en el directorio y generará un archivo CSV llamado `relacion_gastos.csv` en el mismo directorio.

## Estructura del Archivo CSV

El archivo CSV generado contendrá las siguientes columnas:

- **Archivo**: Nombre del archivo XML procesado
- **Fecha**: Fecha de la factura
- **Fecha Corta**: Fecha en formato corto
- **UsoCFDI**: Uso del CFDI
- **RFC Emisor**: RFC del emisor
- **Nombre Emisor**: Nombre del emisor
- **RFC Receptor**: RFC del receptor
- **Nombre Receptor**: Nombre del receptor
- **Descripción**: Descripción del concepto
- **Total**: Total de la factura

## Manejo de Errores

El script maneja errores al procesar archivos XML. Si hay un problema con algún archivo, se imprimirá un mensaje de error y el nombre del archivo problemático.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.