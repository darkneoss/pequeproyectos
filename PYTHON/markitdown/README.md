# Conversor de Archivos a Markdown

Este script en Python permite convertir varios tipos de archivos (documentos, imágenes, audio, etc.) a formato Markdown. Utiliza la biblioteca `markitdown` para realizar la conversión.

## Características

- Soporta múltiples extensiones de archivo, incluyendo:
  - Documentos: `.pdf`, `.pptx`, `.docx`, `.xlsx`
  - Imágenes: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
  - Audio: `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`
  - Otros: `.html`, `.htm`, `.txt`, `.json`, `.xml`, `.zip`
- Salida en archivos `.md` con el mismo nombre que el archivo original.

## Requisitos

- Python 3.x
- Biblioteca `markitdown`

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/darkneoss/pequeproyectos.git
   ```
   
2. Navega al directorio del proyecto:
   ```bash
   cd pequeproyectos
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install markitdown
   ```

## Uso

1. Coloca el script en el mismo directorio donde se encuentran los archivos que deseas convertir.
2. Ejecuta el script desde la línea de comandos:
   ```bash
   python markit.py
   ```

3. El script buscará todos los archivos en el directorio actual que coincidan con las extensiones soportadas (excluyendo el script en sí) y los convertirá a archivos Markdown. Los archivos convertidos se guardarán con la misma base de nombre pero con la extensión `.md`.

## Ejemplo

Supón que tienes los siguientes archivos en el directorio:

```
documento.pdf
imagen.jpg
audio.mp3
script.py
```

Después de ejecutar el script, obtendrás:

```
documento.md
imagen.md
audio.md
```

## Manejo de Errores

- Si no se encuentran archivos para convertir, el script mostrará un mensaje informando que no hay archivos disponibles.
- Si un archivo no se puede convertir debido a un formato no soportado, se mostrará un mensaje de error y el script continuará con el siguiente archivo.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor abre un issue o envía un pull request.