;; TODO -> Update this code

(defun greet (name)
  (concatenate 'string "hello " name))

(defun main ()
  (loop t
    (greet (process-input))
    )

(sb-ext:save-lisp-and-die "hello-world" :executable t :toplevel 'main))
