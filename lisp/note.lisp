(format t "******************** NOTE.LISP ************************~%")

(defpackage :note
  (:use :cl :asdf)
  (:export :sayhi :as-letter :*sharpflat*
	   :note
	   :value :octave :accidental :natural :sharp :flat :+LETTER-VALUES+
	   :eek
	   )
  )

(in-package :note)

(defparameter *sharpflat* 'sharp)
(defparameter *tonic* nil)
(defparameter +LETTER-VALUES+
  '((B+ . C)
    (C+ . D-)
    (D  . D)
    (D+ . E-)
    (E  . F-)
    (E+ . F)
    (F+ . G-)
    (G  . G)
    (G+ . A-)
    (A  . A)
    (A+ . B-)
    (B  . C-)))

(defun as-letter (n)
  (let* ((x (nth (value n) +LETTER-VALUES+))
	 (letter (if (eq *sharpflat* 'sharp)
		    (car x)
		    (cdr x)))
	 (oct (octave n)))
    (if oct
	(format nil "~S~D" letter oct)
	(format nil "~S"   letter))
    ))

(defparameter *note-printer* 'as-letter)


;; 
;; create notes, they contain their value from C in zero, followed by nil or octave
;;
(defclass note ()
  ((value :initarg :value
	  :accessor value
	  :initform 0)
   (octave :initarg :octave
	   :accessor octave
	   :initform nil)
   (accidental :initarg :accidental
	       :accessor accidental
	       :initform 'natural)
   ))

(defmethod initialize-instance :after ((n note) &key)
  (loop 
     while (> (value n) 11)
     do
       (if (octave n)
	   (incf (octave n)))
       (decf (value n) 12))
  (loop 
     while (< (value n) 0)
     do
       (incf (value n) 12)
       (if (octave n) (decf (octave n)))))

(defmethod print-object ((n note) s)
  (write-string (as-letter n) s))

(defun makenote (note value acc)
  (eval `(defparameter ,note (make-instance 'note :value ,value :octave nil :accidental (quote ,acc))))
  (export note)
  (dotimes (i 10)
    (let* ((name (format nil "~S~D" note i))
	   (sym (read-from-string name)))

      (eval `(defparameter ,sym
	     (make-instance 'note 
			    :value ,value 
			    :octave ,i 
			    :accidental (quote ,acc))))
      (export sym)
      )))



(let ((x 0))
  (dolist (pitch '(((B +) (C =))
		   ((C +) (D -)) 
		   ((D =))
		   ((D +) (E -)) 
		   ((E =) (F -)) 
		   ((E +) (F =))
		   ((F +) (G -)) 
		   ((G =)) 
		   ((G +) (A -)) 
		   ((A =))  
		   ((A +) (B -)) 
		   ((B =) (C -))))
    (dolist (n pitch)
      ;(makenote (car pitch) x (cadr pitch))
      (let ((name (read-from-string (format nil "~s~@[~s~]~%" (car n) (if (eq (cadr n) '=) nil (cadr n)))))
	    (acc (cond ((eq (cadr n) '=) 'natural)
		       ((eq (cadr n) '+) 'sharp)
		       ((eq (cadr n) '-) 'flat))))
	(makenote name x acc)
	(format t "~s ~s ~s~%" name acc x)
      ))
    (incf x)))


(defgeneric eek (l r))
(defmethod eek ((l note) (r note))
	   (and (eql (value l) (value r))
		(eql (accidental l) (accidental r))
		(eql (octave l) (octave r))))


