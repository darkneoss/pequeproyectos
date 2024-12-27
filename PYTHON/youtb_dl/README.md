# Video Downloader

This Python script allows you to download videos easily. It uses the `yt-dlp` library, a powerful tool for downloading videos and audio from various streaming platforms.

## Requirements

To run this script, you will need to have Python (3.6 or higher) and the `yt-dlp` library installed. You can install `yt-dlp` using `pip`.

### Installation

1. **Install the dependencies:**

   ```bash
   pip install yt-dlp
   ```

## Usage

1. **Run the script:**

   ```bash
   python youtbdl.py
   ```

2. **Enter the URL of the YouTube video you want to download.**

   The script will validate the URL and start downloading the video into a `downloads` folder, which will be created automatically in the current directory.

## Example Execution

```bash
Enter the URL of the YouTube video to download: https://www.youtube.com/watch?v=example
Downloading video...
Download complete. Video saved in: /path/to/your/directory/downloads
```

## Error Handling

If you enter an invalid URL, the script will inform you and will not proceed with the download. Download errors and other general errors are also handled, displaying an appropriate message if something goes wrong.

## Contributions

Contributions are welcome. If you have suggestions or improvements, feel free to open an issue or a pull request.

---

# Descargador de Videos

Este script en Python permite descargar videos de manera sencilla. Utiliza la biblioteca `yt-dlp`, una potente herramienta para descargar videos y audios de diversas plataformas de streaming.

## Requisitos

Para ejecutar este script, necesitarás tener instalado Python (3.6 o superior) y la biblioteca `yt-dlp`. Puedes instalar `yt-dlp` usando `pip`.

### Instalación

1. **Instala las dependencias:**

   ```bash
   pip install yt-dlp
   ```

## Uso

1. **Ejecuta el script:**

   ```bash
   python youtbdl.py
   ```

2. **Introduce la URL del video de YouTube que deseas descargar.**

   El script validará la URL y comenzará a descargar el video en una carpeta `downloads` que se creará automáticamente en el directorio actual.

## Ejemplo de Ejecución

```bash
Introduce la URL del video de YouTube a descargar: https://www.youtube.com/watch?v=ejemplo
Descargando video...
Descarga completa. Video guardado en: /ruta/a/tu/directorio/downloads
```

## Manejo de Errores

Si introduces una URL no válida, el script te lo indicará y no procederá con la descarga. También se manejan errores de descarga y otros errores generales, mostrando un mensaje adecuado en caso de que ocurra algún problema.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en abrir un issue o un pull request.