(defpackage :tests
  (:use :cl :asdf :lisp-unit :note :interval))

(in-package :tests)

(format t "******************* tests.lisp *****************~%")

(define-test notes ()
	     (assert-equal (value E4) 4)
	     (assert-equal (value B) 11)
	     (assert-equal (as-letter B) "B")
	     (assert-equal (as-letter B+4) "C4")
	     (let ((*sharpflat* 'flat))
	       (assert-equal (format nil "~S" D-7) "D-7")
	       (assert-equal (as-letter B-) "B-")
	       )
	     (assert-equal (format nil "~S" D-6) "C+6")
	     (assert-equal (octave B+4) 4)
	     (assert-equal (octave B) nil)
	     (assert (eek (make-instance 'note
					 :value -1
					 :accidental 'natural
					 :octave 4)
			  (make-instance 'note
					 :value 11
					 :accidental 'natural
					 :octave 3)))
	     
	     (assert-equal (accidental B) 'natural)
	     (assert-equal (accidental B+) 'sharp)
	     (assert-equal (accidental B-) 'flat)
	     (assert (eek (plus C Maj13) A))
	     (assert (equal (print-object C t) "C"))
	     )

(lisp-unit:run-tests)
