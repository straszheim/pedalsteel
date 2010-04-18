
(format t "NOTE ASD ******************************")

(asdf:defsystem "steel"
  :version "0.0.0"
  :maintainer "troy d. straszheim"
  :description "musicy stuff for steel guitar"
  :components ((:file "lisp-unit")
	       (:file "note")
	       (:file "interval" :depends-on ("note"))
	       (:file "tests"    :depends-on ("note" "interval" "lisp-unit"))))


