;; 1. Define a simple class
(defclass person ()
  ((name :initarg :name :accessor person-name)))

;; 2. Create an instance
(defparameter *andy* (make-instance 'person :name "Andy"))

;; 3. Redefine the class to add an 'age' slot
(defclass person ()
  ((name :initarg :name :accessor person-name)
   (age :initform 30 :accessor person-age)))

;; 4. Access the 'age' of the ALREADY EXISTING *andy*
(person-age *andy*)
;; => 30
