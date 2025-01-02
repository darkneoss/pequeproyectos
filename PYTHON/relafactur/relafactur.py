import os
import xml.etree.ElementTree as ET
import csv

def extract_data_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace utilizado en las facturas electrónicas
    ns = {'cfdi': 'http://www.sat.gob.mx/cfd/4'}

    # Datos básicos de la factura
    fecha = root.attrib.get('Fecha')
    fecha_corta = fecha.split('T')[0] if fecha else 'No encontrado'
    total = root.attrib.get('Total')

    # Intentamos encontrar el elemento Emisor y Receptor
    emisor = root.find('cfdi:Emisor', ns)
    receptor = root.find('cfdi:Receptor', ns)
    conceptos = root.find('cfdi:Conceptos', ns)
    descripcion = conceptos.find('cfdi:Concepto', ns).attrib.get('Descripcion') if conceptos is not None else 'No encontrado'
    uso_cfdi = receptor.attrib.get('UsoCFDI') if receptor is not None else 'No encontrado'

    # Verificamos que los elementos existan antes de intentar acceder a sus atributos
    rfc_emisor = emisor.attrib.get('Rfc') if emisor is not None else 'No encontrado'
    nombre_emisor = emisor.attrib.get('Nombre') if emisor is not None else 'No encontrado'
    rfc_receptor = receptor.attrib.get('Rfc') if receptor is not None else 'No encontrado'
    nombre_receptor = receptor.attrib.get('Nombre') if receptor is not None else 'No encontrado'

    return [fecha, fecha_corta, uso_cfdi, rfc_emisor, nombre_emisor, rfc_receptor, nombre_receptor, descripcion, total]

def process_xml_folder():
    # Obtener el directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data = []
    error_files = []
    print(f"Procesando archivos XML en: {script_dir}")
    for file_name in os.listdir(script_dir):
        if file_name.lower().endswith('.xml'):  # Handle file extensions case-insensitively
            xml_path = os.path.join(script_dir, file_name)
            try:
                row = extract_data_from_xml(xml_path)
                row.insert(0, file_name)  # Insert file name as the first column
                data.append(row)
                print(f"Procesado: {file_name}")
            except ET.ParseError as e:
                print(f"Error al parsear {file_name}: {e}")
                error_files.append(file_name)
            except Exception as e:
                print(f"Error procesando {file_name}: {e}")
                error_files.append(file_name)

    if error_files:
        print(f"Archivos con errores: {', '.join(error_files)}")

    return data

def save_to_csv(data, output_file):
    header = ['Archivo', 'Fecha', 'Fecha Corta', 'UsoCFDI', 'RFC Emisor', 'Nombre Emisor', 'RFC Receptor', 'Nombre Receptor', 'Descripcion', 'Total']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data)

# Obtener la ruta del script y definir el archivo de salida
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'relacion_gastos.csv')

data = process_xml_folder()
save_to_csv(data, output_file)

print(f"Datos guardados en {output_file}")
print("\nPresione Enter para cerrar...")
input()
