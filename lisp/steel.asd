
(format t "NOTE ASD ******************************")

(asdf:defsystem "steel"
  :version "0.0.0"
  :maintainer "troy d. straszheim"
  :description "musicy stuff for steel guitar"
  :serial t
  :components (;(:file "util")
	       (:file "lisp-unit")
	       (:file "note")
	       (:file "interval")
	       (:file "tests")))

