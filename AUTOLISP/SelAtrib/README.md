# Selección de Bloques por Atributo en AutoCAD

Este script de AutoLISP permite seleccionar referencias de bloque en AutoCAD basándose en los valores de sus atributos. Es útil cuando necesitas filtrar bloques específicos dentro de un dibujo según los datos que contienen sus atributos.

## Características

*   **Selección por Múltiples Atributos:** Permite seleccionar bloques que coincidan con uno o varios valores específicos en sus atributos.
*   **Interfaz de Usuario:** Utiliza una lista interactiva para seleccionar las etiquetas de atributo deseadas.
*   **Entrada de Valores:** Solicita al usuario los valores correspondientes a cada atributo seleccionado para realizar el filtrado.
*   **Flexibilidad:** Funciona tanto seleccionando objetos en pantalla como en todo el dibujo.
*   **Atribución:** Basado en el código original de VDH-Bruno en [cadxp.com](http://cadxp.com/).

## Cómo usar

1.  **Cargar el Script:**
    *   Abre AutoCAD.
    *   Escribe `APPLOAD` en la línea de comandos y presiona Enter.
    *   Busca y carga el archivo `nombre_del_script.lsp` (reemplaza `nombre_del_script` con el nombre real de tu archivo).
2.  **Ejecutar el Comando:**
    *   Escribe `ssEtVal` en la línea de comandos y presiona Enter.
3.  **Interfaz:**
    *   Aparecerá una lista con todos los campos de atributo disponibles en las definiciones de bloque del dibujo actual.
    *   Selecciona los campos por los que quieres filtrar y haz clic en "Aceptar".
    *   Se te pedirá que introduzcas el valor correspondiente a cada campo seleccionado.
4.  **Selección de Bloques:**
    *   Selecciona los bloques en pantalla sobre los que aplicar el filtro o, pulsa Enter para aplicar el filtro a todo el dibujo.
    *   El script seleccionará los bloques que cumplan con todos los criterios especificados.

## Créditos

Este script es una adaptación del código original de **VDH-Bruno**, publicado en [http://cadxp.com/](http://cadxp.com/index.php?/topic/37573-faire-une-selection-dun-bloc-en-fonction-de-deux-de-ses-attributs/page__pid__207342#entry207342). La adaptación y traducción a español han sido realizadas con el fin de hacer más accesible su uso a la comunidad hispanohablante.

## Dependencias

*   AutoCAD (u otro software compatible con AutoLISP).

## Notas

*   El script utiliza funciones auxiliares (`str2lst` y `ListBox`) para facilitar el manejo de cadenas y la interfaz de usuario.
*   La selección de atributos se basa en las definiciones de atributo presentes en los bloques del dibujo. Asegúrate de que las etiquetas de atributo estén correctamente definidas.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o quieres mejorar el script, no dudes en hacer un pull request.