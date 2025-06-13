## Boolean valus in C89

For many years, C lacked a proper boolean type! :O. Usually C89 programmers often define
macro with names such as TRUE and FALSE

```
#define TRUE 1
#define FALSE 0

if (TRUE) {
	printf("Hey there!");
}
```

We can also extend the above by defining th BOOL macro as follows:

```
#define BOOL int

BOOL is_empty = TRUE;

if (is_empty) {
	printf("It was empty!");
}
```

We can use an enum or type definition instead. We will cover more of this later in the book.

## Boolean values in C99

C99 defines the _Bool type. This type is an unsigned integer.

C99 also introduces <stdbool.h> library which includes several functions to work w/booleans. Adding this header
will allow us to do define variables as this:

```
#include <stdbool.h>

bool is_empty = true;
```
