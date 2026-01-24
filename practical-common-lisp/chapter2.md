# Setting up SLIME

- SLIME = Superior Lisp Interaction Mode for Emacs
- CL development environment built on top of emacs

## First thing to do before using CL

- Choose an implementation
	- Why? Because CL is a standard; And because we don't have a benevolent dictator :), no CPython as default. Need to choose
	- Standard here means : _Contract that tells you that if you write a program that uses the features of the language the way they're described in the standard, you can count on your program behaving the same in any conforming implementation_	


## Implementations
- SBCL = Steel Bank Common Lisp
	- open source. Derived from CMUCL
- Allegro Common Lisp
- OpenMCL
- LispWorks - seems like private

*Note* The book uses allegro in linux

## Is Clojure an implementation of the Common Lisp standard?

- NO :)
- Separate daialect

## Using sly in my emacs

- See more at https://github.com/joaotavora/sly?tab=readme-ov-file
- Seems to be an upgraded version of SLIME

## Notes on LISP

- Every expression evaluates to sht; (format "hello") prints "hello" to stdout
and evaluates to NIL
- When something fails, instead of throwing an exception as in Java or python, you are sent to the debugger. So the language is already telling you since the beginning to debug. Love that :)
