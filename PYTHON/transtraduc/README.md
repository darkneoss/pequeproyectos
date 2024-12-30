# Transcriptor de Audio a Texto con Subtítulos

Este script permite transcribir archivos de audio a texto y generar archivos de subtítulos en formato SRT. Utiliza el modelo Whisper para la transcripción y la API de DeepL para la traducción, si es necesario.

## Requisitos

- Python 3.x
- [whisper](https://github.com/openai/whisper)
- [deepl](https://pypi.org/project/deepl/)
- Dependencias adicionales (pueden ser instaladas usando `pip`):

```bash
pip install -U openai-whisper deepl
```

## Formatos de Audio Soportados

El script busca archivos de audio en el directorio actual con los siguientes formatos:

- WAV
- MP3
- M4A
- FLAC
- OGG

## Uso

1. **Coloca tu archivo de audio** en el mismo directorio que este script.
2. **Ejecuta el script**:

   ```bash
   python transtraduc.py
   ```

3. **Selecciona un modelo** de transcripción. Los modelos disponibles son:
   - `tiny`: El más rápido y ligero (1GB). Precisión básica, ideal para pruebas rápidas.
   - `base`: Modelo equilibrado (1GB). Buena precisión para uso general.
   - `small`: Más preciso que base (2GB). Recomendado para uso diario.
   - `medium`: Alta precisión (5GB). Ideal para contenido profesional.
   - `large`: Máxima precisión (10GB). Mejor calidad pero más lento.

4. **Selecciona el idioma** del audio (1 para español, 2 para inglés).
5. **Opcionalmente**, si seleccionaste inglés, se te preguntará si deseas traducir la transcripción al español.

## Salidas

El script generará los siguientes archivos en el mismo directorio:

- Un archivo de subtítulos SRT con el mismo nombre que el archivo de audio.
- Un archivo de texto con la transcripción completa.
- Si se selecciona la traducción al español, un archivo de texto con la traducción y un archivo SRT traducido.

## Notas

- Asegúrate de tener una clave de autenticación de la API de DeepL para la traducción. Reemplaza `"APIKEY"` en el script con tu clave válida.
- Puede que necesites ajustar la configuración de tu entorno para que funcione correctamente con Whisper y DeepL.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o un pull request.