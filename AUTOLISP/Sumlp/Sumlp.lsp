;; Suma de longitudes de líneas y polilíneas por capa
(defun c:sumlp ()
  (setq ss (ssget '((0 . "LINE,LWPOLYLINE")))) ; Seleccionar líneas y polilíneas
  (if ss
    (progn
      (setq layers_info '()) ; Lista para almacenar información por capa
      (setq total_general 0.0) ; Total general de longitud

      (setq i 0)
      (repeat (sslength ss)
        (setq ent (ssname ss i))
        (setq ent_data (entget ent))
        (setq layer (cdr (assoc 8 ent_data)))  ; Obtener el nombre de la capa
        (setq longitud (vlax-curve-getDistAtParam ent (vlax-curve-getEndParam ent))) ; Obtener longitud
        
        ; Buscar si ya existe la capa en la lista
        (setq found nil)
        (foreach layer_info layers_info
            (if (equal (car layer_info) layer)
                (progn
                  (setq found t)
                  (setq longitud_acumulada (+ (cadr layer_info) longitud))
                  (setq layers_info (subst (list layer longitud_acumulada) layer_info layers_info)) ; Actualizar la longitud
                  )
            )
        )
        ; Si la capa no existe, agregarla a la lista
        (if (not found)
            (setq layers_info (append layers_info (list (list layer longitud))))
        )
        
        (setq total_general (+ total_general longitud)) ; Acumular longitud total
        (setq i (1+ i))
      )

      ; Imprimir el resumen por capa
      (princ "\nResumen de Longitudes por Capa:\n")
      (princ "-----------------------------------\n")
      (foreach layer_info layers_info
        (princ (strcat "Capa: " (car layer_info) ", Longitud: " (rtos (cadr layer_info) 2 3) "\n"))
      )
      (princ "-----------------------------------\n")
      (princ (strcat "Longitud Total General: " (rtos total_general 2 3) "\n")) ; Imprimir la longitud total con 3 decimales
    )
    (princ "\nNo se seleccionaron líneas o polilíneas.\n")
  )
  (princ)
)
