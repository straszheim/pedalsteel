(format t "******************** CHORD.LISP ************************~%")

(defmacro without-package-variance-warnings (&body body)
  `(eval-when (:compile-toplevel :load-toplevel :execute)
     (handler-bind (#+sbcl(sb-int:package-at-variance #'muffle-warning))
       ,@body)))

(without-package-variance-warnings
    (defpackage :chord
      (:use :cl :asdf :note :interval)
;      (:export :sayhi :as-letter :*sharpflat*
;	       :note
;	       :value :octave :accidental :natural :sharp :flat :+LETTER-VALUES+
;	       :eek
	       ))

(in-package :chord)

(defparameter +chord+ '((*maj  Per1 Maj3 Per5)
			(*min  Per1 Min3 Per5)
			(*maj7 Per1 Maj3 Per5 Maj7)
			(*min7 Per1 Min3 Per5 Min7)
			(*dom7 Per1 Maj3 Per5 Min7)
			))

(defmacro make-chord (ch &rest notes)
  "Construct a function that converts a note into the notes of the chord"
  `(defun ,ch (n)
     (mapcar (lambda (x) (plus n x)) (list ,@notes))))

(dolist (i +chord+)
  (destructuring-bind (sym . ivals) i
    (format t "~S => ~S~%" sym ivals)
    (eval `(defparameter ,sym (list ,@ivals)))
    (eval `(make-chord ,sym ,@ivals))
    (export sym)
    ))
