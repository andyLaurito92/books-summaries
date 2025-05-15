# Unix System overview

## Kernel vs Operating system

Kernel -> 
- Core component of an operating system
- Reponsible for managing the computer's hardware resources (processor, memory, I/O devices)
- Provides interface for apps to communicate w/hardware
- Enforces security policies to protect the system

Operating system ->
- Collection of software programs taht work together to provide a complete computing environment
- Includes Kernel + device drivers, user interfaces, libraries and utilities
- Interface for users to interact with the computer
- Manages the resources of the system, including memory, storage and input/output devices

Linux is an open-source project that provides a free kernel that can be used *as the foundation*
for building operating systems.

Example of O.S. that include Linux as kernel -> Ubuntu, Fedora and Debian

Link to [linux repo](https://github.com/torvalds/linux)


*Interface to the kernel = system calls*

Libraries of common functions are built on top of the system calls interface

- Shell: Special application that provides an interface fonr running other apps


### UNIX

Unix is an operating system created in AT&T Bell labs in 1970. Even O.S. with no connections
to Uix take a lot of cues from UNIX regarding basic operations. It is the originator of 
the concept of files and directories, for example.

Linux was originally made in 1991 to be an open source reimplementation of Unix, back when 
Unix itself was still closed source and not really available outside of academia.

A decade later, Apple shifted from their own completely propietary O.S. backend to their 
own brand of Unix, where they made heave alterations (which they open sourced) and called it
Darwin. This become the basis of both OSX and iOS.

### Loggin in

We log in to a UNIX system -> Look up of login name + password in /etc/password

root:*:0:0:System Administrator:/var/root:/bin/sh

1. Root is the login name
2. Password, lives in a different file.
3. user id
4. Group id
5. Comment, in the above: System administrator
6. Home directory
7. Default shell

*Question:* My user doesn't appear there, why?

In the meantime, there are 2 commands in Darwin that show at least my user:

- users
- who

Output of who

```
NAME             LINE         TIME         FROM
andreslaurito    console      31 Dec 13:49 
andreslaurito    ttys000      20 Jan 06:13 
andreslaurito    ttys001      28 Apr 15:55 
andreslaurito    ttys002      25 Apr 07:00 
andreslaurito    ttys003      28 Apr 15:59 
```

### Shells

Shell -> command line interpreter, written in C. Calls directly syscalls from O.S. 

*TODO: Implement a silly one in C*

#### A bit of history

|                    |           |              |             |                |           |
| Name               | Path      | FreeBSD      | Linux 3.2.0 | Mac OSX 10.6.8 | Solaris10 |
| Bourne Shell       | /bin/sh   | *            | *           | bash           | *         |
| Bourne-again-shell | /bin/bash | optional     | *           | *              | *         |
| C Shell            | /bin/csh  | link to tcsh | optional    | link to tcsh   | *         |
| Korn shell         | /bin/ksh  | optional     | optional    | *              | *         |
| TENEX C shell      | /bin/tcsh | *            | optional    | *              | *         |


- Bourne shell -> Developed by Steve Bourne at Bell labs. Control flow are reminiscent of Algol 68
- C shell -> 
  - Bill Joy at Berkely, provided w/BSD releases
  - Its control flow looks more like the C language
  - Supports additional features, such as:
	- Job control
	- History mechanism
	- Command line argument
  - Note: You can find this shell in Darwin :)
- Korn is compatible w/bourne, not much to say. Not that used
- Bourne-again shell: Is the GNU shell provided w/all linux systems
	- Designed to be POSIX performant
	- Compatible w/Bourne shell
	- Supports features from both Bourne and Korn shell
	
Shell was standardized in the POSIX 1003.2 standard 

*Note:* Remember that we tampered diversification w/standardisation :)


### Files and directories

#### Directory

- File that contains directory entries
- Logically: Entry that contains: filename, attributes

The attributes are: Type of the file, size, owner, permissions for the file, last modified. 

Use *stat* to see the attributes of a file
Use *file* to see the coding of the file + the type

When directory created, 2 files are created: . (current dir) and .. (parent dir)


You can list all files in a directory by using *ls*. 

*Note* An example of a C implementation of ls can be seen in myls.c script. 
To compile it, you can use cc, which is the c/c++ compiler

*Note* When we login, our home directory is obtained from our entry in the pwd file -> *TODO: Confirm this*

### Input/Output

#### File Descriptors

Small non-negative integer that the kernel uses to identify the files accessed by a process.
Whenever it opens an existing file or creates a new file, the kernel returns a file
descriptor that we use  when we want to read or write the file.

### stdin, stdout, stderr

By convention, all shells open 3 descriptors:
- standard input 
- standard output
- standard error

By default, all three are connected to the terminal

To redirect use >, for example: `ls > file.list` #redirect stdout to file

### unbuffered io

see open, read, write, lseek and close

When we use `head < myfile.txt`, we are redirecting standard input from myfile.txt instead of 
normal standard input

### Program vs Processes

#### Program

Executable file residing on disk in a directory. 

A program is read into memory and is executed by the kernel 
as a result of noe of the seven exec functions

#### Process

An executing instance of a program

*Example:* See process_ex.c under code folder

When you run 

```
cc process_ex.c
./a.out
```
The above:
- Looks for process_ex.c (file) in disk
- Loads program into memory
- Executes the code (run instructions)

There are 2 ways of creating a process:
1. fork
2. exec: This function has 7 variants :)

And one for waiting for its termination:

1. waitpid

Remember that forks is called once (in the parent) and
returned twice: 1 in the child (w/pid = 0) and 1 in the parent (w/pid = child pi > 0)

#### Threads

Set of machine instructions executing at a time. 

Threads within a process share the same address space, file descriptors, stacks, and
process-related attributes. Each thread executes on its own stack, although any 
thread can access the stacks of other threads in the same process. 

This is why we need to synchronize threads, because they can access the same memory
space than other threads :)
