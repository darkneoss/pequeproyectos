import whisper
import os
import time
import deepl

def find_audio_file():
    supported_formats = ['wav', 'mp3', 'm4a', 'flac', 'ogg', 'MP3']
    for file in os.listdir():
        if any(file.endswith(f'.{ext}') for ext in supported_formats):
            return file
    return None

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{int(seconds):02d},{milliseconds:03d}"

def create_srt_content(segments):
    srt_content = ""
    for i, segment in enumerate(segments, start=1):
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text'].strip()
        srt_content += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"
    return srt_content

def select_model():
    models = {
        1: ("tiny", "El más rápido y ligero (1GB). Precisión básica, ideal para pruebas rápidas."),
        2: ("base", "Modelo equilibrado (1GB). Buena precisión para uso general."),
        3: ("small", "Más preciso que base (2GB). Recomendado para uso diario."),
        4: ("medium", "Alta precisión (5GB). Ideal para contenido profesional."),
        5: ("large", "Máxima precisión (10GB). Mejor calidad pero más lento.")
    }
    
    print("\nModelos disponibles:")
    for num, (model_name, description) in models.items():
        print(f"{num}. {model_name}: {description}")
    
    while True:
        try:
            choice = int(input("\nSeleccione el número del modelo (1-5): "))
            if choice in models:
                return models[choice][0]
            print("Por favor, seleccione un número válido (1-5)")
        except ValueError:
            print("Por favor, ingrese un número válido")

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)
current_directory = os.getcwd()
print(f"Directorio de trabajo actual: {current_directory}")

audio_file_name = find_audio_file()
if not audio_file_name:
    print("No se encontró ningún archivo de audio en el directorio del script.")
    exit()

audio_file_path = os.path.join(current_directory, audio_file_name)
print(f"Archivo de audio encontrado: {audio_file_path}")

# Selección del modelo
print("Cargando el modelo Whisper...")
selected_model = select_model()
model = whisper.load_model(selected_model)
print(f"Modelo '{selected_model}' cargado con éxito.")

# Solicitar idioma al usuario
while True:
    language_choice = input("Ingrese el número del idioma del audio (1 para español, 2 para inglés): ")
    if language_choice == "1":
        audio_language = "es"
        break
    elif language_choice == "2":
        audio_language = "en"
        break
    else:
        print("Por favor, ingrese 1 o 2.")

print("Iniciando transcripción...")
start_time = time.time()
result = model.transcribe(audio_file_path, fp16=False, language=audio_language)
end_time = time.time()
print("Transcripción completada.")

transcription_time = end_time - start_time
transcription_time_minutes = transcription_time / 60
print(f"Tiempo de transcripción: {transcription_time_minutes:.2f} minutos")

# Generar contenido SRT
srt_content = create_srt_content(result["segments"])

# Guardar archivo SRT
srt_file_name = os.path.splitext(audio_file_name)[0] + '.srt'
srt_file_path = os.path.join(current_directory, srt_file_name)
with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
    srt_file.write(srt_content)
print(f"Archivo de subtítulos SRT guardado en {srt_file_path}")

# Guardar transcripción completa en formato de texto
transcription = result["text"]
txt_file_name = os.path.splitext(audio_file_name)[0] + '_transcription.txt'
txt_file_path = os.path.join(current_directory, txt_file_name)
with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(transcription)
print(f"Transcripción completa guardada en {txt_file_path}")

# Traducir la transcripción al español si el usuario lo solicita
if language_choice == "2":
    translate_choice = input("¿Desea traducir la transcripción al español? (s/n): ")
    if translate_choice.lower() == "s":
        print("Traduciendo la transcripción al español...")
        
        # Utilizar la API de DeepL para traducir
        auth_key = "APIKEY"  # Reemplaza con tu clave de autenticación
        translator = deepl.Translator(auth_key)
        
        translated_result = translator.translate_text(transcription, target_lang="ES")
        
        # Guardar la transcripción traducida en un archivo separado
        translated_txt_file_name = os.path.splitext(audio_file_name)[0] + '_transcription_es.txt'
        translated_txt_file_path = os.path.join(current_directory, translated_txt_file_name)
        with open(translated_txt_file_path, 'w', encoding='utf-8') as translated_txt_file:
            translated_txt_file.write(translated_result.text)
        
        print(f"Transcripción traducida al español guardada en {translated_txt_file_path}")
        
        # Traducir los subtítulos SRT
        translated_srt_content = create_srt_content([
            {"start": segment["start"], "end": segment["end"], "text": translator.translate_text(segment["text"], target_lang="ES").text}
            for segment in result["segments"]
        ])
        
        translated_srt_file_name = os.path.splitext(audio_file_name)[0] + '_subtitles_es.srt'
        translated_srt_file_path = os.path.join(current_directory, translated_srt_file_name)
        with open(translated_srt_file_path, 'w', encoding='utf-8') as translated_srt_file:
            translated_srt_file.write(translated_srt_content)
        
        print(f"Archivo de subtítulos SRT traducido al español guardado en {translated_srt_file_path}")

input("Presiona Enter para cerrar...")