(vl-load-com)

(defun round (num)
  (if (>= (- num (fix num)) 0.5)
    (1+ (fix num))
    (fix num)
  )
)

;; Poner etiquetas de longitud y tramo en las polilíneas seleccionadas
(defun c:et (/ ss i ent len midpt angle dx dy tramo_prefix start_num do_table table_data ent_data p_angle offset base_ang txt_len txt_tramo p1 p2 mspace)
  (setq offset 1.5) ; Distancia desde la línea al texto
  
  ;; Preguntas al usuario
  (initget "Si No")
  (setq do_num (getkword "\n¿Numerar tramos? [Si/No] <No>: "))
  (if (not do_num) (setq do_num "No"))
  
  (if (= do_num "Si")
    (progn
      (setq start_num (getint "\nNúmero inicial <0>: "))
      (if (not start_num) (setq start_num 0))
    )
  )

  (initget "Si No")
  (setq do_table (getkword "\n¿Insertar tabla? [Si/No] <No>: "))
  (if (not do_table) (setq do_table "No"))

  (princ "\nSeleccione las polílíneas: ")
  (if (not (setq ss (ssget '((0 . "LWPOLYLINE")))))
    (setq ss (ssget "P" '((0 . "LWPOLYLINE"))))
  )

  (if ss
    (progn
      (setq i 0)
      (setq table_data nil)
      (while (< i (sslength ss))
        (setq ent (ssname ss i))
        (setq len (vlax-curve-getDistAtParam ent (vlax-curve-getEndParam ent)))
        (setq len (round len))
        
        (setq midpt (vlax-curve-getPointAtParam ent (/ (vlax-curve-getEndParam ent) 2)))
        (setq dx (car (vlax-curve-getFirstDeriv ent (/ (vlax-curve-getEndParam ent) 2))))
        (setq dy (cadr (vlax-curve-getFirstDeriv ent (/ (vlax-curve-getEndParam ent) 2))))
        (setq angle (atan dy dx))
        
        (setq base_ang angle)
        ;; Normalizar ángulo para lectura de texto
        (if (or (> angle (/ pi 2)) (<= angle (- (/ pi 2))))
          (setq angle (+ angle pi))
        )

        (setq p_angle (+ base_ang (/ pi 2))) ; Angulo perpendicular
        
        ;; Crear Etiqueta de Tramo (Arriba)
        (if (= do_num "Si")
          (progn
            (setq txt_tramo (strcat "T" (itoa start_num)))
            (setq p1 (polar midpt p_angle offset))
            (entmake
              (list
                (cons 0 "TEXT")
                (cons 10 p1) ; Punto de inserción (será ignorado por alineación si 11 existe)
                (cons 11 p1) ; Punto de alineación
                (cons 40 2.5)
                (cons 1 txt_tramo)
                (cons 50 angle)
                (cons 7 "Standard")
                (cons 8 "E - TEXT TRAMO")
                (cons 72 1) ; Center
                (cons 73 1) ; Bottom
              )
            )
            (setq table_data (cons (list txt_tramo (itoa len)) table_data))
            (setq start_num (1+ start_num))
          )
          (setq table_data (cons (list (strcat "P" (itoa i)) (itoa len)) table_data))
        )

        ;; Crear Etiqueta de Longitud (Debajo)
        (setq txt_len (strcat (itoa len) "m"))
        (setq p2 (polar midpt (+ p_angle pi) offset))
        (entmake
          (list
            (cons 0 "TEXT")
            (cons 10 p2)
            (cons 11 p2)
            (cons 40 2.5)
            (cons 1 txt_len)
            (cons 50 angle)
            (cons 7 "Standard")
            (cons 8 "E - TEXT LONG")
            (cons 72 1) ; Center
            (cons 73 3) ; Top
          )
        )
        
        (setq i (1+ i))
      )

      ;; Insertar Tabla
      (if (and (= do_table "Si") table_data)
        (progn
          (setq ins_pt (getpoint "\nPunto de inserción de la tabla: "))
          (if ins_pt
            (progn
              (setq mspace (vla-get-modelspace (vla-get-activedocument (vlax-get-acad-object))))
              (setq table_obj (vla-addtable mspace (vlax-3d-point ins_pt) (+ 2 (length table_data)) 2 10.0 40.0))
              (vla-settext table_obj 0 0 "RESUMEN DE TRAMOS")
              (vla-settext table_obj 1 0 "TRAMO")
              (vla-settext table_obj 1 1 "LONGITUD (m)")
              
              (setq table_data (reverse table_data))
              (setq row 2)
              (foreach data table_data
                (vla-settext table_obj row 0 (car data))
                (vla-settext table_obj row 1 (cadr data))
                (setq row (1+ row))
              )
            )
          )
        )
      )
    )
  )
  (princ "\nComando ET completado.")
  (princ)
)