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
