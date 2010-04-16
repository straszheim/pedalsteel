;;;; -*- Mode: Lisp; Syntax: ANSI-Common-Lisp; Base: 10 -*-

(defpackage #:note-asd
  (:use :cl :asdf))

(in-package :note-asd)

(defsystem note
  :name "note"
  :version "0.0.0"
  :maintainer "troy d. straszheim"
  :description "notes and stuff"
  :serial t
  :components ((:file "note")))

