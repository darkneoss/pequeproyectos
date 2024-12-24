import os
import sys
from markitdown import MarkItDown

def main():
    # Nombre del script
    script_name = os.path.basename(__file__)
    
    # Listar todos los archivos en el directorio actual
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f != script_name]
    
    # Verificar que solo hay un archivo
    if len(files) != 1:
        print("Error: Debe haber exactamente un archivo en el directorio junto al script.")
        print(f"Archivos encontrados: {files}")
        sys.exit(1)
    
    # Obtener el nombre del archivo
    input_file = files[0]
    output_file = os.path.splitext(input_file)[0] + '.md'  # Crear nombre para el archivo de salida
    
    print(f"Convirtiendo {input_file} a Markdown...")
    
    try:
        # Inicializar MarkItDown
        md = MarkItDown()
        
        # Realizar la conversión
        result = md.convert(input_file)
        
        # Guardar el contenido convertido en un archivo Markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        print(f"Conversión completa. Archivo guardado como: {output_file}")
    
    except Exception as e:
        print(f"Error al convertir el archivo: {str(e)}")

if __name__ == "__main__":
    main()
