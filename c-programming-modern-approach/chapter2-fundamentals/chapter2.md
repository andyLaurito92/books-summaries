## Compiling and Linking

Let's brush up these 2 main concepts :)

1. *Preprocessing*: The program is first given to a preprocessor, which obeys commands that begin with # (known as directives).
A preprocessor is a bit like an editor. You can get the preprocessing output by running `cc -E hello_world.c -o hello_world.i`
2. *Compiling*: The modified program now goes to a compiler, which translates it into machine instructions (object code). This is the compiled
binary. This is binary machine code + symbols (not linked yet). This is the step after assembly
3. *Linking*: Final step, a linker combines the object code produced by the compiler w/any additional code needed to yield a complete
executable program. Ex: Include library functions

In order to run the hello_word.c example, just run
`cc hello_world.c -o helloworld`

And then execute it using ./helloworld

### Getting deeper into the Matrix (compilation/build process) - This is out of scope from the book

On this section, I'll get depeer on how compilers internally work. For developers, to compile means to go from source code to 
object code/binary/.jar/whatever format can be executed by some platform (jvm, my OS, whatever). 

For a compiler, "compiling" means frontend parses + type checks -> IR -> Optimizer -> backend -> assembly

The real compilation steps are these ones:

[1] Preprocessing (macros, includes)
    hello.c  →  hello.i

[2] Compiler Frontend (parsing, semantic analysis)
    hello.i  →  IR (e.g. LLVM IR) (.ll)

[3] Compiler Backend (optimizations + codegen)
    IR (.ll)      →  Assembly (.s)

[4] Assembler
    .s       →  Object file (.o)

[5] Linker
    .o       →  Executable


Let's go into one of them.

#### Preprocessing

- Handles #include, #define, #if and macro expansions. These are call directives and are commands for the preprocessor.
- Remove comments
- Produces preprocessed source (.i file)

`cc -E hello_world.c -o hello_world.i`

Example of directive: `#include <stdio.h>`

*Note:* In C you can either do `#include <stdio.h>` or `#include "stdio.h"`. What's the difference?

- `#include <sht>` Looks for something only in the system include libraries
- `#include "sht.h"` Looks first in the current directory and then, if not found, in the system include libraries

#### Compiler frontend

- Translates preprocessed C code into a intermediate representation (LLVM IR)
- Produces .ll file
- The output is in text format! Still readable by humans :)

`cc -S -emit-llvm hello_world.c -o hello_world.ll`


#### Assembly code

Human readable. Assembly based on the platform you are working at

`cc -S hello_world.ll -o hello_world.s` or `cc -S hello_world.c -o hello_world.s`

#### Object file

`cc -c hello_world.c -o hello_world.o`

This generates object code, a bit file for the specific platform, BUT not executable yet :O

#### Linker

- Combine all object files into a same executable
- Resolve symbols: The linker finds all symbol definitions (function names/variables) and refernces and
matches them so the executable knows where each function or variable lives
- Link libraries, such as .so or .dylib
- Assign final addresses into memory
- Produces executable or library

`cc hello_world.o -o hello_world`

Usually there are 2 system linkers: `ld` on Unix-like systems, or the LLVM linker `lld`


*Note* clang and cc are intercheangable. cc is a symlink to clang in OSX.

clang is a new compiler (started around 2007) as part of the LLVM project!. It was backed up by Apple
and uses a frontend LLVM's modular compiler backend architecture. 

On the other hand, gcc is older (1980s), is owned by the free software foundations, and uses a
traditional monolithic compiler design.


## Functions

The book treat function as a collection of statemens :) 

- main is a mandatory function that is called automatically when the program is executed
- main returns the status code of the program. This value is returned to the operating system (different from Java!)

*Note* main is not really mandatory but "recommended" by the ISO standard. What it really triggers the call to the main function
is the *C runtime libraty (CRT)*: These aren't anything else than libraries that are linked into your program in the linker process. 
Usually, these routines are shipped as part of the compiler and reside in the `crt0.o`, `crt1.o` or `crtbegin.o` object file

This startup code usually:
- Set up the environment (e.g. stack, heap, command-line arguments)
- Calls `main(argc, argv, envp)`
- Takes the return value of `main` and passes it to the O.S.

*Note* _statements_ end w/; while _directives_ don't (ex: `#include`)

## Macros

When you use either `#define` or `#include`, you are defining *MACROS* of the preprocessor. 

*What does this mean?* Same as what it means in Lisp! The preprocessor reads the macro, and it replaces it w/the code that 
it represents. In this case, `#define` just means _"Replaces this for that"_

*Important* C has constants, which are defined as `const char* messsage = "Thanks user!"`. The're a lot of differences between
defining a macro and a constant in this case:

- A `#define` is never seen by the compiler given that it's a macro interpreted by the preprocessor
- It doesn't have neither type nor space in memory, as `const char*` does
- Usually preferred `const char*` than `#define` for maintainability

## printf

### Conversion specificacions 

- Begin with % character
- Placeholder representing the value to fill. The information that follows the % character 
specifies how the value is converted from its interna from (binary) to printed form (characters)
*Example:* printf("%d", &i); is telling printf that it needs to convert an int value from binary to a string
of decimal digits
- %m.pf -> print m digits before . and p digits after . . If fewer digits than m are provided, then the value is
right justified.
