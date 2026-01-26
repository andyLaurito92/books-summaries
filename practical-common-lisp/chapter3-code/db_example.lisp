;; Creating a database of books

(list 1 2 3) ;; Create a simple list

(defparameter x
  (list :a 1 :b 2 :c 3)
  ) ;; property list/map

(print (getf x :b))

(defun make-book (title author numpages)
  (list :title title :author author :numpages numpages))

;; Okay, so far we can create records but where do we store them?
;; Let's introduce a global variable

(defvar *bookcase* nil) ;; global variables are defined between *

(defun add-record (abook)
  (push abook *bookcase*)) ;; push is a macro

(defun dump-db ()
  (dolist (book *bookcase*) ;; dolist is a macro
    (format t "~{~a:~10t~a~%~}~%" book))) ;; What the heck is this doing? :)

;; *query-io* contains the input stream connected to the terminal
;; global variable, as u can see from **
(defun prompt-read (prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(defun parse-integer-or-get-default-numpages ()
  (or
    (parse-integer (prompt-read "Numpages") :junk-allowed t)
    0) ;; short-circuiting for now to define default value
  )

(defun prompt-for-book ()
  (make-book
    (prompt-read "Title")
    (prompt-read "Author")
    (parse-integer-or-get-default-numpages)
    ))
