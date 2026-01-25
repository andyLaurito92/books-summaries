(list 1 2 3) ;; Create a simple list

(defparameter x
  (list :a 1 :b 2 :c 3)
  ) ;; property list/map

(print (getf x :b))
