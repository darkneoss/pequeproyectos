import os
from markitdown import MarkItDown
import sys
from markitdown._markitdown import UnsupportedFormatException  # Importa la excepción específica


def main():
    # Cambiar el directorio de trabajo al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Nombre del script
    script_name = os.path.basename(__file__)

    # Lista de extensiones de archivos soportadas (ajusta según tus necesidades)
    supported_extensions = (
        '.pdf', '.pptx', '.docx', '.xlsx',
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff',
        '.mp3', '.wav', '.ogg', '.flac', '.m4a',
        '.html', '.htm',
        '.txt', '.json', '.xml',
        '.zip'
    )
    
    # Lista todos los archivos en el directorio actual que coinciden con las extensiones
    files_to_convert = [f for f in os.listdir('.') 
                       if os.path.isfile(f) and f != script_name and f.lower().endswith(supported_extensions)]
    
    # Verifica si hay archivos para convertir
    if not files_to_convert:
        print("No se encontraron archivos para convertir en el directorio.")
        input("Presiona cualquier tecla para cerrar...")
        return
    
    # Inicializar MarkItDown (sin cliente LLM)
    md = MarkItDown()
    
    total_files = len(files_to_convert)
    for i, file in enumerate(files_to_convert):
        print(f"\nConvirtiendo {file} a Markdown... ({i+1}/{total_files})")
        try:
            # Construir el nombre del archivo de salida .md
            output_file = os.path.splitext(file)[0] + '.md'
            
            # Realizar la conversión
            result = md.convert(file)
            
            # Guardar el contenido convertido en un archivo Markdown
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            print(f"Conversión completa. Archivo guardado como: {output_file}")
        except UnsupportedFormatException as e:  # Captura la excepción específica
            print(f"Error al convertir el archivo {file}: {str(e)}")
            print(f"Saltando el archivo {file} y continuando con el siguiente.")
            continue
        except Exception as e: # Cualquier otro error desconocido
            print(f"Error desconocido al convertir {file}: {str(e)}")
            print(f"Saltando el archivo {file} y continuando con el siguiente.")
            continue

    print("\nTodas las conversiones completadas!")
    input("Presiona cualquier tecla para cerrar...")

if __name__ == "__main__":
    main()
