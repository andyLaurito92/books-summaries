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

Linux was originally made in 1991 to be an oper source reimplementation of Unix, back when 
Unix itself was still closed source and not really available outside of academia.

A decade later, Apple shifted from their own completely propietary O.S. backend to their 
own brand of Unix, where they made heave alterations (which they open sourced) and called it
Darwin. This become the basis of both OSX and iOS.
