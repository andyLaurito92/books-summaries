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

