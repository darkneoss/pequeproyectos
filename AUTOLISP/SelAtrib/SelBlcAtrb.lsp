;; 
;; http://cadxp.com/index.php?/topic/37573-faire-une-selection-dun-bloc-en-fonction-de-deux-de-ses-attributs/page__pid__207342#entry207342 
;; 
;; Rutina por VDH-Bruno                                    le: 28/05/2013
;; ======================================================================
;; Selección de referencias de bloque en función de las etiquetas de atributo
;; y sus valores específicos.

;;
;; Traducción Francés ---> Español
;;

(defun c:ssEtVal (/ lstTagAtt tagAtt doc ss1 ss2 inclu-p inputval)
  (vl-load-com)
  (setq doc (vla-get-ActiveDocument (vlax-get-acad-object))
        ss2 (ssadd)
  )

  ;; Lista los nombres de las definiciones de atributo de la tabla de bloques
  (vlax-for b (vla-get-Blocks doc)
    (if (and (= (vla-get-IsLayout B) :vlax-false)
             (= (vla-get-IsXref B) :vlax-false)
             (not (wcmatch (vla-get-Name B) "*|*"))
        )
      (vlax-for o b
        (and (= (vla-get-ObjectName o) "AcDbAttributeDefinition")
             (not (member (setq tagAtt (vla-get-TagString o)) lstTagAtt))
             (setq lstTagAtt (cons tagAtt lstTagAtt))
        )
      )
    )
  )

  ;; Muestra la lista en una caja de lista para selección múltiple
  (setq
    lstTagAtt (listbox 
                  "Campos/Columnas de Atributo"  ; Traducido "Attribute Fields/Columns"
                  "Seleccione los Campos/Columnas de Atributo a filtrar..." ; Traducido "Select the Attribute Fields/Columns to Filter..."
                (mapcar 'cons (setq lstTagAtt (vl-sort lstTagAtt '<)) lstTagAtt)
                2
              )
  )

  ;; Valores a asociar a las etiquetas correspondientes
  (defun inputval (l)
    (if l
      (cons
        (cons
          (car l) 
          (getstring (strcat "Valor a buscar para el Campo/Columna " (car l) ": ")) ; Traducido "Value to search for the Fields/Columns"
        )
        (inputval (cdr l))
      )
    )
  )

  (cond
    ((setq lstTagAtt (inputval lstTagAtt))

     ;; Definición de la zona de selección 
     (princ "\nSeleccione los bloques o <Todo>: ")  ; Traducido "Select the Blocks or <all> : " 
     (or (ssget (list '(0 . "INSERT") '(66 . 1)))
         (ssget "_X" (list '(0 . "INSERT") '(66 . 1)))
     )

     ;; Predicado de inclusión de una lista l1 en otra lista l2
     (defun inclu-p (l1 l2)
       (cond ((null l1) t)
             ((member (car l1) l2) (inclu-p (cdr l1) l2))
             (t nil)
       )
     )

     ;; Filtrado de la selección
     (vlax-for b (setq ss1 (vla-get-ActiveSelectionSet doc))
       ;; verifica que los criterios de filtro (Tag .Val) están incluidos en el bloque
       (if (inclu-p
             lstTagAtt
             ;; Lista las parejas (Tag .Val) de la referencia de bloque   
             (mapcar
               '(lambda (x) (cons (vla-get-TagString x) (vla-get-TextString x)))
               (vlax-invoke b 'GetAttributes)
             )
           )
         (ssadd (vlax-vla-object->ename B) ss2)
       )
     )
     (vla-delete ss1)
     (sssetfirst nil ss2)
    )
  )
  (princ)
)


;;;;;;;;;;;;;;; 
;; Las rutinas asociadas a cargar antes de la función principal
;;;;;;;;;;;;;;; 

;;============================================================================;;

;; STR2LST
;; Transforma una cadena con separador en lista de cadenas
;;
;; Argumentos
;; str : la cadena a transformar en lista
;; sep : el separador

;;
;; Ejemplos
;; (str2lst "a b c" " ") -> ("a" "b" "c")
;; (str2lst "1,2,3" ",") -> ("1" "2" "3")
;; (mapcar 'read (str2lst "1,2,3" ",")) -> (1 2 3)

(defun str2lst (str sep / pos)
  (if (setq pos (vl-string-search sep str))
    (cons (substr str 1 pos)
          (str2lst (substr str (+ (strlen sep) pos 1)) sep)
    )
    (list str)
  )
)

 
;; ListBox por GC 
;; Caja de diálogo que permite una o varias selecciones en una lista
;;
;; Argumentos
;; title : el título de la caja de diálogo (cadena)
;; msg ; mensaje (cadena), "" o nil para ninguno
;; keylab : una lista de asociación del tipo ((clave1 . etiqueta1) (clave2 . etiqueta2) ...)
;; flag : 0 = lista desplegable
;;        1 = lista selección única
;;        2 = lista selección múltiple
;;
;; Retorno : la clave de la opción (flag = 0 o 1) o la lista de las claves de las opciones (flag = 2)
;;
;; Ejemplo de uso
;; (listbox "Presentación" "Elegir una presentación" (mapcar 'cons (layoutlist) (layoutlist)) 1)
 
 
(defun ListBox (title msg keylab flag / tmp file dcl_id choice)
  (setq        tmp  (vl-filename-mktemp "tmp.dcl")
                    file (open tmp "w")
  )
  (write-line
    (strcat "ListBox:dialog{label=\"" title "\";")
    file
  )
  (if (and msg (/= msg ""))
    (write-line (strcat ":text{label=\"" msg "\";}") file)
  )
  (write-line
    (cond
      ((= 0 flag) "spacer;:popup_list{key=\"lst\";")
      ((= 1 flag) "spacer;:list_box{key=\"lst\";")
      (T "spacer;:list_box{key=\"lst\";multiple_select=true;")
    )
    file
  )
  (write-line "}spacer;ok_cancel;}" file)
  (close file)
  (setq dcl_id (load_dialog tmp))
  (if (not (new_dialog "ListBox" dcl_id))
    (exit)
  )
  (start_list "lst")
  (mapcar 'add_list (mapcar 'cdr keylab))
  (end_list)
  (action_tile
    "accept"
    "(or (= (get_tile \"lst\") \"\")
    (if (= 2 flag) (progn
    (foreach n (str2lst (get_tile \"lst\") \" \")
    (setq choice (cons (nth (atoi n) (mapcar 'car keylab)) choice)))
    (setq choice (reverse choice)))
    (setq choice (nth (atoi (get_tile \"lst\")) (mapcar 'car keylab)))))
    (done_dialog)"
  )
  (start_dialog)
  (unload_dialog dcl_id)
  (vl-file-delete tmp)
  choice
)
