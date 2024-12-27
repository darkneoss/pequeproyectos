# Suma Longitud de Líneas y Polilíneas por Capa (sumlp.lsp)

Este script de AutoLISP para AutoCAD permite seleccionar líneas y polilíneas y calcula la longitud total de las mismas, agrupadas por capa.

## Descripción

El script `sumlp.lsp` realiza las siguientes acciones:

1.  **Selecciona Entidades:** Pide al usuario que seleccione líneas y polilíneas en el dibujo de AutoCAD.
2.  **Calcula Longitud por Capa:** Calcula la longitud de cada línea y polilínea seleccionada, acumulando las longitudes por capa.
3.  **Almacena Información:** Guarda la capa y la longitud acumulada de cada capa en una lista.
4.  **Muestra Resumen por Capa:** Imprime en la línea de comandos un resumen de las longitudes acumuladas por cada capa.
5.  **Muestra Longitud Total General:** Imprime la longitud total de todas las líneas y polilíneas seleccionadas.
6.  **Manejo de Errores:** Muestra un mensaje si no se selecciona ninguna línea o polilínea.

## Cómo Utilizar

1.  **Carga el Script:**
    *   Abre AutoCAD.
    *   Escribe `APPLOAD` en la línea de comandos y presiona Enter.
    *   Navega hasta donde guardaste el archivo `sumlp.lsp`, selecciónalo y haz clic en "Cargar".
    *   Cierra la ventana de "Cargar/Descargar Aplicaciones".

2.  **Ejecuta el Comando:**
    *   Escribe `SUMPL` (o `sumlp` si AutoCAD no distingue mayúsculas) en la línea de comandos y presiona Enter.
    *   Selecciona las líneas y polilíneas que deseas sumar.
    *   Presiona Enter para finalizar la selección.

3.  **Visualiza los Resultados:**
    *   El script imprimirá en la línea de comandos un resumen de las longitudes por capa, y la longitud total general.

## Ejemplo de Salida

Resumen de Longitudes por Capa:
```
Capa: 0, Longitud: 15.789
Capa: A-WALL, Longitud: 32.456
Capa: A-DOOR, Longitud: 10.123
Longitud Total General: 58.368
```

---

