# PDF Blank Page Remover

This Python script removes blank pages from PDF files in the current directory and saves the processed files in a folder called `processed`.

## Requirements

Make sure you have Python installed on your system. This script requires the `PyPDF2` library. You can install it using `pip`:

```bash
pip install PyPDF2
```

## Usage

1. Place the `remove_blank_pages.py` script in the directory where the PDF files you want to process are located.
2. Run the script:

```bash
python remove_blank_pages.py
```

3. The script will create a folder named `processed` in the same directory, where it will save the PDF files without the blank pages. The files will be named with the prefix `processed_`.

## Example

If you have a file named `document.pdf` in the same directory as the script, and it contains some blank pages, when you run the script, it will create a file named `processed_document.pdf` in the `processed` folder, which will not contain the blank pages.

## Functionality

- **is_blank_page(page)**: Function that checks if a page is blank.
- **remove_blank_pages(pdf_path, output_path)**: Function that processes a PDF file and removes blank pages, saving the result to a new file.
- **process_pdfs_in_directory()**: Function that iterates through all PDF files in the current directory, processing them and saving the results in the `processed` folder.

## Contributions

Contributions are welcome. If you would like to improve this script, please open an issue or submit a pull request.

---

# Eliminador de Páginas en Blanco de PDFs

Este script de Python elimina las páginas en blanco de archivos PDF en el directorio actual y guarda los archivos procesados en una carpeta llamada `processed`.

## Requisitos

Asegúrate de tener Python instalado en tu sistema. Este script requiere la biblioteca `PyPDF2`. Puedes instalarla usando `pip`:

```bash
pip install PyPDF2
```

## Uso

1. Coloca el script `remove_blank_pages.py` en el directorio donde se encuentran los archivos PDF que deseas procesar.
2. Ejecuta el script:

```bash
python remove_blank_pages.py
```

3. El script creará una carpeta llamada `processed` en el mismo directorio, donde se guardarán los archivos PDF sin las páginas en blanco. Los archivos se nombrarán con el prefijo `processed_`.

## Ejemplo

Si tienes un archivo llamado `documento.pdf` en el mismo directorio que el script y este contiene algunas páginas en blanco, al ejecutar el script, se creará un archivo llamado `processed_documento.pdf` en la carpeta `processed`, que no contendrá las páginas en blanco.

## Funcionalidad

- **is_blank_page(page)**: Función que verifica si una página está en blanco.
- **remove_blank_pages(pdf_path, output_path)**: Función que procesa un archivo PDF y elimina las páginas en blanco, guardando el resultado en un nuevo archivo.
- **process_pdfs_in_directory()**: Función que itera a través de todos los archivos PDF en el directorio actual, procesándolos y guardando los resultados en la carpeta `processed`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este script, por favor, abre un issue o envía un pull request.
