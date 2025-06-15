## One-dimensional arrays

- Arrays in C have elements of all the same type

To declare an array, we do it like this:

```
int a[10];
```

or by using a macro

```
#define ARR_SIZE 10;
int a[ARR_SIZE]; 
```

### The out-of memory error in C

```
int main(void) {
  int a[10], i;
  for (i = 1; i <= 10; i++)
    a[i] = 0;
}
```

This program *might* return `Abort trap: 6` when trying to run it or run "fine". The issue is that you are writing out of boundaries in the
array. 

Note that the issue is being triggered by the O.S., in this case macOS, and not the C compiler itself (that's why you are able
to compile the above code without any issue).

Nowadays, making the above program to run actually is not that easy. The O.S. has many safeguards against out of memory issues. Examples of these are:
1. Writing a guard page placed after your local variable
2. Compiler has a stack protection enabled (`-fstack-protector`)
3. Your O.S. might use DEP/NX (no-execute stack) and ASLR, making
corruption more likely to crash predictabily

There are also stack canaries, guard pages, memory poisionoing tooks and so on to catch these type of bugs early.

In order to run the above code, use the following flags while compiling:

```
cc -fno-stack-protector -O0 out_bounds_arr.c
```

`-O` stands up for optimization. You are telling the compiler to
not optimize your code, also telling: "Keep it as close as the code as 
possible". Other options are:

- -O1: basic optimization -> faster builds
- -O2: good optimization -> production
- -O3: Aggresive optimization -> performance-critical code
- -Os: Optimize for size -> embedded systems
- -Ofast: All -03 + unsafe FP optimizations

### Address Space Layout Randomization (ASLR)

Security feature that randomizes memory locations at runtime, to make buffer overflows and memory exploits harder.
