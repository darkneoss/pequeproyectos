(defun c:ChBl (/ ss ent blk newblk pt sc ang)
  (setq newblk (getstring "\nNombre del bloque nuevo: "))
  
  ;; Verificar si hay una selección previa
  (setq ss (ssget "I"))
  (if (null ss)
    ;; Si no hay selección, permitir al usuario seleccionar
    (progn
      (princ "\nSeleccione los bloques a cambiar: ")
      (setq ss (ssget '((0 . "INSERT"))))
    )
  )
  
  (if ss
    (progn
      (setvar "CMDECHO" 0)
      (command "._UNDO" "_BEGIN")
      
      ;; Procesar cada bloque seleccionado
      (setq i 0)
      (repeat (sslength ss)
        (setq ent (ssname ss i))
        (if (= (cdr (assoc 0 (entget ent))) "INSERT")
          (progn
            (setq blk (entget ent))
            ;; Obtener propiedades del bloque original
            (setq pt (cdr (assoc 10 blk)))     ;; Punto de inserción
            (setq sc (cdr (assoc 41 blk)))     ;; Escala X
            (setq ang (cdr (assoc 50 blk)))    ;; Ángulo de rotación
            
            ;; Insertar nuevo bloque con las mismas propiedades
            (command "._INSERT" newblk pt sc sc ang)
            ;; Borrar bloque original
            (entdel ent)
          )
        )
        (setq i (1+ i))
      )
      
      (command "._UNDO" "_END")
      (setvar "CMDECHO" 1)
      (princ "\nBloques cambiados exitosamente.")
    )
    (princ "\nNo se seleccionaron bloques.")
  )
  (princ)
)