# Script AutoLISP para Extracción de Datos de Bloques

## Descripción

`ExtCordBlk` es un script AutoLISP diseñado para extraer información relevante de los bloques en un dibujo de AutoCAD y, opcionalmente, exportar esos datos a un archivo CSV.

El script realiza las siguientes acciones:

1.  **Selecciona Bloques:** Permite al usuario seleccionar todos los bloques presentes en el dibujo actual.
2.  **Extrae Datos:** Para cada bloque seleccionado, extrae:
    *   Nombre del bloque.
    *   Capa en la que se encuentra el bloque.
    *   Coordenadas X e Y de su punto de inserción.
    *   Rotación del bloque en grados.
3.  **Muestra en Pantalla:** Imprime en la línea de comandos de AutoCAD la información de cada bloque.
4.  **Exportación a CSV (Opcional):** Pregunta al usuario si desea exportar los datos a un archivo CSV. Si la respuesta es afirmativa, permite seleccionar la ubicación y nombre del archivo. El CSV incluye un encabezado con los nombres de las columnas.

## Uso

1.  Carga el script en AutoCAD usando el comando `APPLOAD` o arrastrando el archivo `ExtCordBlk.lsp` a la ventana de AutoCAD.
2.  Escribe `exb` en la línea de comandos y presiona `Enter`.
3.  El script seleccionará todos los bloques del dibujo.
4.  Revisa la línea de comandos para ver la información extraída de cada bloque.
5.  Si se te pregunta, elige si quieres exportar la información a un archivo CSV. Si eliges exportar, selecciona la ubicación donde guardar el archivo.

## Formato del Archivo CSV

El archivo CSV generado tendrá el siguiente formato:

```csv
Bloque,Capa,X,Y,Rotation
NombreBloque1,Capa1,123.45,456.78,0.00
NombreBloque2,Capa2,789.01,234.56,90.00
```

*   `Bloque`: Nombre del bloque.
*   `Capa`: Capa en la que se encuentra el bloque.
*   `X`: Coordenada X del punto de inserción del bloque.
*   `Y`: Coordenada Y del punto de inserción del bloque.
*   `Rotation`: Rotación del bloque en grados.

## Consideraciones

*   Este script asume que los bloques son inserciones directas en el dibujo, no dentro de otros bloques.
*   La precisión de las coordenadas en el archivo CSV es de dos decimales.
*   El archivo CSV se guardará en la ubicación que elija el usuario.

## Contribuciones

Si encuentras errores, mejoras que hacer, o quieres agregar funcionalidades, ¡las contribuciones son bienvenidas! Puedes hacerlo a través de pull requests.

