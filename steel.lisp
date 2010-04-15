;;
;;  gimpy test suite
;;
(use-package :lisp-unit)

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
   (as-string :initarg :as-string
	      :accessor as-string
	      :initform (error "specify string name"))
   (accidental :initarg :accidental
	       :accessor accidental
	       :initform 'natural)
   ))

(trace makenote)
(defun makenote (note value acc)
  (eval `(defparameter ,note (make-instance 'note :value ,value :octave nil :as-string ,(symbol-name note) :accidental (quote ,acc))))
  (dotimes (i 10)
    (let ((name (format nil "~S~D" note i)))
    (eval `(defparameter ,(read-from-string name) 
	     (make-instance 'note 
			    :value ,value 
			    :octave ,i 
			    :as-string ,name 
			    :accidental (quote ,acc)))))))

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
	(format t "~s ~s ~s" name acc x)
      ))
    (incf x)))

(describe C-)

(defmethod print-object ((n note) s)
  (write-string (as-string n) s))

(define-test notes ()
  (assert-equal (value E4) 4)
  (assert-equal (value B) 11)
  )

(run-tests)

(deftest test-n ()
  (combine-results (test-notes)))


(test-n)

;;
;; create intervals, they contain their value in halfsteps
;;
(defparameter intervals '((U1   0  1 'perfect)
			  (MI2  1  2 'minor)
			  (MA2  2  2 'major)
			  (MI3  3  3 'minor)
			  (MA3  4  3 'major)
			  (P4   5  4 'perfect)
			  (A4   6  4 'augmented)
			  (D5   6  5 'diminished)
			  (P5   7  5 'perfect)
			  (MI6  8  6 'minor)
			  (MA6  9  6 'major)
			  (MI7  10 7 'minor)
			  (MA7  11 7 'major)
			  (P8   12 8 'perfect)
			  (MI9  13 9 'minor)
			  (Ma9  14 9 'major)
			  (MI10 15 10 'minor)
			  (MA10 16 10 'major)
			  (P11  17 11 'perfect)
			  (A11  18 11 'augmented)
			  (D12  18 12 'diminished)
			  (P12  19 12 'perfect)
			  (MI13 20 13 'minor)
			  (MA13 21 13 'major)))

(defclass interval ()
  ((halfsteps :initarg :halfsteps
	      :accessor halfsteps)
   (steps     :initarg :steps
	      :accessor steps)
   (modifier  :initarg :modifier
	      :accessor modifier)
   (as-string :initarg :as-string
	      :accessor as-string)))

(dolist (i intervals)
  ;(let ((sym (nth 0 i))
  ;(hsteps (nth 1 i))
  ;(wsteps (nth 2 i))
  ;(type (nth 3 i)))
  (destructuring-bind (sym hsteps wsteps type) i
    (format t "~S ~S ~S ~S~%" sym hsteps wsteps type)
    (eval `(defparameter ,sym (make-instance 'interval
					     :halfsteps ,hsteps 
					     :steps ,wsteps 
					     :modifier ,type
					     :as-string ,(symbol-name sym))))))

(defmethod print-object ((i interval) s)
  (write-string (as-string i) s)
  )

(defclass neck ()
  ((tuning :initarg :tuning :accessor tuning)
   (pedals :initarg :pedals :accessor pedals)))

(defconstant nada '(0 0 0 0 0  0 0 0 0 0))
(defconstant E9-neck
  (make-instance 'neck
		 :tuning '( B2  D3  E3  F+3 G+3   B3  E4  G+4 D+4 F+4)

		 :pedals `((p1 . (+2   0   0   0   0    +2   0   0   0   0)) 
			   (p2 . ( 0   0   0   0  +1     0   0  +1   0   0)) 
			   (p3 . ( 0   0   0   0   0    +2  +2   0   0   0))
			   (p4 . ( 0   0   0   0  -2    -2   0   0   0   0))
			   (p5 . ,nada)
			   (p6 . ,nada)
			   (p7 . ,nada)
			   (p8 . ,nada)

			   (ll . ( 0   0  +1   0   0     0  +1   0   0   0))
			   (lu . (-1   0   0   0   0    -1   0   0   0   0))
			   (lr . ( 0   0  -1   0   0     0  -1   0   0   0))
			   (rl . ( 0   0   0  +2   0     0   0   0   0  +2))
			   (rr . ( 0   0   0   0   0     0   0   0  -2   0)))))

  


(defclass change ()
  ((deltas :initarg :deltas
	   :accessor deltas)))

(setf p1 (make-instance 'change :deltas '(0 1 0 1)))

(plus E3 2)

(defvar p1)
(deltas p1)
(setf (deltas p1) 333)

(setf (neck-tuning n) 'foooooooooo)
(neck-tuning n)

(describe p1)

(class-of p1)

(defvar *sharpflat* 'sharp)

(defconstant letter-values 
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
  (let* ((x (nth (value n) letter-values))
	 (letter (if (eq *sharpflat* 'sharp)
		    (car x)
		    (cdr x)))
	 (oct (octave n)))
    (if oct
	(format nil "~S~D" letter oct)
	(format nil "~S"   letter))
    ))

(defparameter *sharpflat* 'sharp)

D+7

(print-object ma2)

(defvar *sharpflat* 'flat)
somenote

(setf somenote (make-instance 'note :value 8 :octave nil))
(defconstant D (make-instance 'note :value 2 :octave nil))
(defconstant E (make-instance 'note :value 4 :octave nil))
(defconstant E3 (make-instance 'note :value 4 :octave 3))

E

(format t "~S" E)

(describe E)

(describe 'print-object)


(defconstant ma2 (make-instance 'interval :value 2))
(defconstant mi2 (make-instance 'interval :value 1))

(defgeneric plus (arg1 arg2))

(defmethod plus ((arg1 note) (arg2 interval))
  (format nil "plus ~S ~S" arg1 arg2))

(defmethod plus ((arg1 note) (arg2 note))
  (format nil "plusnote ~S ~S" arg1 arg2))

(defmethod plus ((arg1 note) (arg2 integer))
  (format nil "plusnote ~S ~S" arg1 arg2))

(setf x 3)
(describe x)
(plus E ma2)
(plus E E)

(plus E 17)
(value E)
(value mi2)

(trace plus)

(setf v #(1 2 3 4 5))

v

(defmethod plus ((arg1 note) (arg2 #(interval)))
  
  )


(setf v2 #(1 2 3 ))

(describe v2)

(vector 1 2 3)
