# Etiquetado Automático de Tramos para Planos de Alumbrado

Este script de AutoLISP permite etiquetar automáticamente longitudes de tramos y generar una tabla resumen.

## Características

- **Etiquetado Automático**: Añade etiquetas de longitud a polilíneas seleccionadas.
- **Numeración de Tramos**: Opción para numerar secuencialmente los tramos.
- **Generación de Tabla**: Crea una tabla de resumen con los tramos y sus longitudes.
- **Personalización**: Configurable para adaptarse a diferentes estilos de documentación.
- **Eficiencia**: Reduce el tiempo de etiquetado manual y minimiza errores.

## Cómo Usar

### Instalación

1. Abre AutoCAD
2. Escribe `APPLOAD` en la línea de comandos
3. Carga el archivo `LabelSect.lsp`

### Ejecución del Comando

1. Escribe `ET` en la línea de comandos
2. Sigue los prompts interactivos:
   - Selecciona si quieres numerar tramos
   - Elige el número inicial de tramo
   - Decide si quieres generar una tabla de resumen
3. Selecciona las polilíneas a etiquetar
4. Confirma la ubicación de la tabla (si aplica)

### Ejemplo de Flujo

```
Comando: ET
¿Numerar tramos? [Si/No]: Si
Número inicial <0>: 1
¿Insertar tabla? [Si/No]: Si
Seleccione las polílíneas: [Selección múltiple]
Punto de inserción de la tabla: [Clic en ubicación]
```

## Requisitos

- AutoCAD con soporte de AutoLISP
- Polilíneas definidas en el dibujo
- Versión de AutoCAD compatible con AutoLISP

## Personalización

- Ajusta el `offset` para modificar la distancia del texto
- Configura capas de texto según tus necesidades de diseño

## Limitaciones

- Funciona únicamente con polilíneas
- Requiere polilíneas correctamente definidas
- Compatibilidad puede variar según la versión de AutoCAD


