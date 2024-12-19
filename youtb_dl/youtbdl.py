import os
import yt_dlp
import re

def download_youtube_video():
    # Crear una carpeta 'downloads' para guardar el video
    download_folder = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_folder, exist_ok=True)

    # Solicitar URL del video
    video_url = input("Introduce la URL del video de YouTube a descargar: ")

    # Validar URL
    if not re.match(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+', video_url):
        print("URL no válida. Por favor, introduce una URL de YouTube válida.")
        return

    try:
        # Configuración para la descarga
        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }

        # Descargar el video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nDescargando video...")
            ydl.download([video_url])

        print(f"\nDescarga completa. Video guardado en: {download_folder}")

    except yt_dlp.utils.DownloadError as e:
        print(f"\nError de descarga: {e}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

if __name__ == "__main__":
    download_youtube_video()
