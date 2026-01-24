;; First, create sly session by C-x S

;; Evaluate using C-x C-e
(+ 2 2)
"hey"

;; Send function using C-c C-c
(defun hello ()
  (print "hey!")
  )

;; Note: "Sending" lines as in python is not the way?
