## History

- Comes from Bell Laboratories, developed in the early 1970s. 
- C comes from the UNIX operating system (initially written in assembly, later moved to C)
- The C programming language book was published in 1978! :O
- The ANSI C standard, referred as C89 or C90, was standardised in 1990. The original C version is also called K&R C
- In 1999 a new standard was made. This standard is referred as C99

## Strengths & weaknesses

- C is a low-level langauge: C provides access to machine-level concepts (bytes anda ddresses, for example) that other
programming language try to hide. C also provides operations that correspond closely to a computer's built-in instructions,
so that programs can be fast.
- Efficiency: It's super fast :) Was meant to replace assembler
- Portability: Thanks to be associated w/Unix
- Integration w/UNIX

Not so good things of C

- C programs can be error-prone: flexibility comes w/a price

## Some useful tools to use w/your C programs

- lint: Linter for c
- bound-checkers: Checking bounds when accessing memory
- leak-finders: Finding memory leaks

### Concrete examples on the above tools

#### Linters

1. [clang-tidy](https://clang.llvm.org/extra/clang-tidy/)
2. [cppcheck](https://cppcheck.sourceforge.io/)
3. Use gcc/clang w/extra flags, such as `-Wall -Wextra -Wpedantic -Wshadow -Wundef -Wconversion -Werror`

#### Memory leak detectors

1. Valgrind

