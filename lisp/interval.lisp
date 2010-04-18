(format t "************ interval.lisp **************~%")

(defpackage :interval
  (:use :cl :asdf :note)
  (:export +intervals+ :plus)
  )

(in-package :interval)

;; ;;
;; ;; create intervals, they contain their value in halfsteps
;; ;;
(defparameter +intervals+ '((PER1  0  1 'perfect)
			    (MIN2  1  2 'minor)
			    (MAJ2  2  2 'major)
			    (MIN3  3  3 'minor)
			    (MAJ3  4  3 'major)
			    (PER4  5  4 'perfect)
			    (AUG4  6  4 'augmented)
			    (DIM5  6  5 'diminished)
			    (PER5  7  5 'perfect)
			    (MIN6  8  6 'minor)
			    (MAJ6  9  6 'major)
			    (MIN7  10 7 'minor)
			    (MAJ7  11 7 'major)
			    (PER8  12 8 'perfect)
			    (MIN9  13 9 'minor)
			    (MAJ9  14 9 'major)
			    (MIN10 15 10 'minor)
			    (MAJ10 16 10 'major)
			    (PER11 17 11 'perfect)
			    (AUG11 18 11 'augmented)
			    (DIM12 18 12 'diminished)
			    (PER12 19 12 'perfect)
			    (MIN13 20 13 'minor)
			    (MAJ13 21 13 'major)))

(defclass interval ()
  ((halfsteps :initarg :halfsteps
	      :accessor halfsteps)
   (steps     :initarg :steps
	      :accessor steps)
   (modifier  :initarg :modifier
	      :accessor modifier)
   (as-string :initarg :as-string
	      :accessor as-string)))

(dolist (i +intervals+)
  ;(let ((sym (nth 0 i))
  ;(hsteps (nth 1 i))
  ;(wsteps (nth 2 i))
  ;(type (nth 3 i)))
  (destructuring-bind (sym hsteps wsteps type) i
    (format t "~S ~S ~S ~S~%" sym hsteps wsteps type)
    (let ((inst (make-instance 'interval 
			       :halfsteps hsteps
			       :steps wsteps
			       :modifier type
			       :as-string (symbol-name sym))))
      (eval `(defparameter ,sym ,inst))
      (export sym))))

(defmethod print-object ((i interval) s)
  (write-string (as-string i) s)
  )

(defgeneric plus (arg1 arg))

(defmethod plus ((n note) (i interval))
  (make-instance 'note 
		 :value (+ (value n) (halfsteps i))
		 :octave (octave n)
		 :accidental (accidental n)))

