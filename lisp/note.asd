;;;; -*- Mode: Lisp; Syntax: ANSI-Common-Lisp; Base: 10 -*-

(format t "NOTE ASD ******************************")

(asdf:defsystem note
  :name "note"
  :version "0.0.0"
  :maintainer "troy d. straszheim"
  :description "notes and stuff"
  :serial t
  :components ((:file "lisp-unit")
	       (:file "note")))

