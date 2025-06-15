K.N.King book. I'll be using it as a brush up on C so I can better grasp the content of advanced programming in unix

Kings webpage can be found [here](http://knking.com/). Resources of this book can be found at this [link](http://knking.com/books/c2/)

## Why learning C?

Without knowing that much, it seems like C is the Operating system language. Many O.S. are written in C:

- [XNU](https://github.com/apple-oss-distributions/xnu): The kernel for the Darwin O.S. (macOS)
- [Linux](https://github.com/torvalds/linux): In reality, linux is hosted here: https://git.kernel.org/, the github repo is just a mirror
- [FreeBSD](https://github.com/freebsd/freebsd-src)

Without saying that many of the known programming languages nowadays, such as Java or Python, have in it's core C :)

- [cpython](https://github.com/python/cpython)
- [opnejdk](https://github.com/freebsd)
- [emacs](https://github.com/emacs-mirror/emacs) (github mirror, original repo [here](https://cgit.git.savannah.gnu.org/cgit/emacs.git/))
- [erlang/otp](https://github.com/erlang/otp)
- [LLVM](https://github.com/llvm/llvm-project) - C++ compiler (one of the many implementations of C++)

You also have your favorite tools written in C :)

- [curl](https://github.com/curl/curl/tree/master/lib): Link to libcurl, the library which contains all the logic for implementing the 
different application protocols that curl knows how to handle

From the above, it also makes sense to say that C will usually be part of the core of a programming language. Let's say you want to build your 
own language: You will need a core that communicates to the O.S. and implements all the IO functions we 99% of the times use :) C will probably
be what you want to use in such a case!

So my take away: Learn C to get deeper into stuff. Welcome to un-explore territory :D


### More about C

C is still the main language for embedded systems. It seems that the reason is both historical and for predictability: C is a super small and
compact language that is super close to the hardware. It's easier to use when your problem has a direct match w/hardware (ex: Arduino, embedded
systems, ...). 

It's not necessarily true that C always performs better than C++. C++ has compiler optimizations and other stuff that make it sometimes even faster
than C. The problem with these last features is that C++ becomes less predictable then!

I see C as a good option when no programming abastractions are needed for your code. Example: Let's say that you want to implement an algorithm that
will be used by a piece of your system. U coding in Java/Python/Kotlin/whatever and u thinking in coding it there? Think twice! If it's some sort of
algorithm that won't change and needs to be fast, might be better to have a compiled C version of it and make your application program to call this 
compiled object instead.


## Miscelaneous

Flag `-W` is for warnings in the gcc/clang compiler. Usual options are:

- `-Wall` (-W=warnings all): Show all warnings
- `-Wextra` Enable extra warnings not included in all
- `-Wparentheses` (-W=warnings parentheses)
- `-Weverything` Super verbose, but might be useful for specific ocassions

The family of options is:

- Enable specific warnings: `-W<name>`
- Disable warning: `-Wno-<name>`
- Treat warnings as errors: `-Werror[=<name>]`
- Control the level of diagnostic and strictness

Usual recommendations:

- Use `-Wall -Wextra`
- Use `-Werror` in a CI/CD pipeline
- Use `-Weverything` for specific cases


## Other References besides this book

- https://github.com/dunamismax/C-From-the-Ground-Up---A-Project-Based-Approach : Interesting repo that walks you through different projects in C for building stuff and augmenting knowledge
