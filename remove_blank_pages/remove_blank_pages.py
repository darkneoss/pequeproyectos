# -*- coding: utf-8 -*-

import os
from PyPDF2 import PdfReader, PdfWriter

def is_blank_page(page):
    # Verifica si la página está en blanco comparando su contenido de texto
    text = page.extract_text()
    return not text.strip()

def remove_blank_pages(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    # Añade todas las páginas que no estén en blanco
    for page in reader.pages:
        if not is_blank_page(page):
            writer.add_page(page)
    
    with open(output_path, 'wb') as output_pdf:
        writer.write(output_pdf)

def process_pdfs_in_directory():
    # Obtiene la ruta del directorio actual donde se encuentra el script
    directory_path = os.path.dirname(os.path.abspath(__file__))
    
    # Crea una carpeta 'processed' dentro del directorio actual
    processed_dir = os.path.join(directory_path, 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            input_path = os.path.join(directory_path, filename)
            output_path = os.path.join(processed_dir, f"processed_{filename}")
            remove_blank_pages(input_path, output_path)
            print(f"Processed {filename}")

# Ejemplo de uso
process_pdfs_in_directory()

input("Presiona Enter para cerrar...")
