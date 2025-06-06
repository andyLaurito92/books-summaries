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

### Getting deeper into the Matrix (compilation/build process)

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

- Handles #include, #define, #if and macro expansions.
- Remove comments
- Produces preprocessed source (.i file)

`cc -E hello_world.c -o hello_world.i`

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
