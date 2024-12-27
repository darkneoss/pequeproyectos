(defun c:exb ()
  (setq ss (ssget '((0 . "INSERT")))) ; Selecciona todos los bloques
  (if ss
    (progn
      (setq n (sslength ss))
      (setq data-list nil) ; Inicializa la lista para almacenar los datos
      (repeat n
        (setq ent (ssname ss (setq n (- n 1))))
        (setq data (entget ent))
        
        ;; Obtener el nombre del bloque
        (setq blockname (cdr (assoc 2 data))) ; Nombre del bloque
        ;; Obtener las coordenadas del bloque
        (setq coords (cdr (assoc 10 data))) ; Coordenadas del bloque
        ;; Obtener la capa del bloque
        (setq layer (cdr (assoc 8 data)))    ; Capa del bloque
        ;; Obtener la rotación del bloque en grados
        (setq rotation (cdr (assoc 50 data))) ; Rotación del bloque en radianes
        (setq rotation-grados (angtos rotation 0 0)); Convertir a grados

        ;; Imprimir el nombre, coordenadas, capa y rotación
        (princ (strcat "\nBloque: " blockname ", Capa: " layer ", " 
                       (rtos (car coords) 2 2) ", " 
                       (rtos (cadr coords) 2 2) ", "
                       rotation-grados)) ; Mostrar la rotación en grados

        ;; Almacenar datos en la lista
        (setq data-list (cons (list blockname layer (rtos (car coords) 2 2) (rtos (cadr coords) 2 2) rotation-grados) data-list))
      )
      
      ;; Limpiar el buffer de entrada ANTES de getstring
      (terpri)
      
      ;; Pregunta si quiere exportar a csv
      (setq exportar (getstring "\n¿Desea exportar la información a CSV? (s/n): "))
      (if (or (= exportar "s") (= exportar "S"))
        (exportar-a-csv data-list)
      )
    )
    (princ "\nNo se seleccionaron bloques.")
  )
  (princ)
)

(defun exportar-a-csv (data-list)
  (setq filename (getfiled "Guardar datos como CSV" "" "csv" 1))
  (if filename
    (progn
      (setq file (open filename "w"))
      (if file
        (progn
          (write-line "Bloque,Capa,X,Y,Rotation" file) ; Escribir encabezado con el nombre de Bloque
          (foreach item data-list
            (write-line (strcat (nth 0 item) "," (nth 1 item) "," (nth 2 item) "," (nth 3 item) "," (nth 4 item)) file)
          )
          (close file)
          (princ (strcat "\nDatos exportados a: " filename))
        )
        (princ "\nError al abrir el archivo.")
      )
    )
    (princ "\nNo se especificó un nombre de archivo.")
  )
)
