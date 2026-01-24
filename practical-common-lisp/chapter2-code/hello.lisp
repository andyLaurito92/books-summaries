;; First, create sly session by C-x S
;; To open documentation, C-c h over a function/expression

;; Evaluate using C-x C-e
(+ 2 2)
"hey"

;; Send function using C-c C-c
(defun hello ()
  (print "hey!")
  )

;; Note: "Sending" lines as in python is not the way?

;; To install libraries, you do it from the REPL
(ql:quickload :dexador)

;; To use it, you can do
(dex:get "https://google.com")

(format t "hello word") ;; Prints to standard output and returns NIL

(print "hello")

(defun hey (name)
  (concatenate 'string "Hello " name))

;; To load a file use the load function
; (load "hello.lisp ")

;; fasl -> fast load file
(defparameter *compile-file-name* 
  (compile-file "hello.lisp")) ;; This will compile hello.lisp to hello.fasl

(print *compile-file-name*)

;; Notes
;; 1 -> Use defparameter to define global variables. Convention, between **
;; 2 -> To load file using a command: C-c C-l -> sly-load-file
;; 3 -> C-c C-k to compile & load the current file


;; If you want to see the assembly code of a defined function
(disassemble 'hey)
