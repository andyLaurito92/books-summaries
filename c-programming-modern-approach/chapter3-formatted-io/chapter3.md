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

## Order on function definition

You need to declare functions before they're being used. This is bc how C works. If you don't follow this, then 
you will get an error in the compiler frontend phase, concretely, in the semantic analysis phase.
