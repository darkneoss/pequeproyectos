# Script de AutoLISP: Cambiar Bloques

Este script de AutoLISP permite reemplazar bloques en un dibujo de AutoCAD por un nuevo bloque especificado por el usuario, manteniendo las propiedades de inserción, escala y rotación del bloque original.

## Descripción

El script permite al usuario seleccionar uno o varios bloques en el dibujo y luego, al proporcionar el nombre de un nuevo bloque, reemplaza cada bloque seleccionado por el nuevo bloque con las mismas propiedades de posición, escala y rotación.

## Funcionalidades

- Permite seleccionar bloques existentes en el dibujo.
- Solicita al usuario el nombre de un nuevo bloque.
- Reemplaza los bloques seleccionados manteniendo las propiedades del bloque original.
- Utiliza comandos de deshacer para asegurar que los cambios puedan revertirse si es necesario.

## Requisitos

- AutoCAD con soporte para scripts de AutoLISP.

## Instrucciones de uso

1. **Carga el script en AutoCAD**:
   - Abre AutoCAD.
   - Ejecuta el comando `APPLOAD` y selecciona este archivo de script.

2. **Ejecuta el comando**:
   - Escribe `ChBl` en la línea de comandos y presiona Enter.

3. **Selecciona los bloques**:
   - Si no hay selección previa, se te pedirá que selecciones los bloques a cambiar. Puedes seleccionar varios bloques a la vez.

4. **Ingresa el nombre del nuevo bloque**:
   - Cuando se te solicite, escribe el nombre del nuevo bloque que deseas insertar y presiona Enter.

5. **Revisión**:
   - El script reemplazará los bloques seleccionados y mostrará un mensaje de éxito o informará si no se seleccionaron bloques.

## Ejemplo

Supongamos que tienes un bloque llamado `AntiguoBloque` y deseas reemplazarlo por `NuevoBloque`. Simplemente ejecuta el script, selecciona `AntiguoBloque`, ingresa `NuevoBloque` cuando se te pida, y todos los bloques seleccionados serán reemplazados.

## Notas

- Asegúrate de que el nuevo bloque esté definido en el dibujo antes de ejecutar el script.
- Este script utiliza el comando `UNDO` para permitir deshacer los cambios realizados.
- No esta soportado el uso de bloques con atributos .

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en abrir un issue o un pull request.
