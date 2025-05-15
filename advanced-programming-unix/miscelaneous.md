## Some useful commands to know

- *vmmap*: virtual memory map, use this command to know the memory distribution of a process.
Keys to remember about this command: User space memory, Kernel space memory, remember that 
malloc is a user function from the C library and not the system call that actually assigns
memory :)

The above tool is useful for identifying fragmentation

- *lsof*: List open files of a process. Without any flag, list all open files given a process (-p PID)
Given that mostly everything is a file in Linux based O.S., this gives you info about the open 
sockets, files (REG), tcp connections

Example of usage: `sudo lsof -iTCP -sTCP:ESTABLISHED -nP`


-n means don't resolve IPs to hostnames (no DNS resolution)

- *netstat* List all open internet sockets 

- *file* Tells you the type of the file, usage: `file script.py`

- *tcpdump* To see a continuos dump of all TCP happening in your machine

- *fs_usage* file system usage, lists system calls related to filesystem.
Usage example: `sudo fs_usage firefox`

- *sample* Profile a process. From the man page:
```
sample is a command-line tool for gathering data about the running behavior of a process.  It suspends the process at specified intervals (by default, every 1 millisecond), records the call
     stacks of all threads in the process at that time, then resumes the process.  The analysis done by sample is called ``sampling'' because it only checks the state of the program at the
     sampling points.  The analysis may miss execution of some functions that are not executing during one of the samples, but sample still provides useful data about commonly executing functions.
```
Ex of usage: `sample <PID> -f output.txt`

Note: The call graph will show stacktrace of user space code, not kernel space.

- *dig* DNS lookup utility. Example of usages:
`dig +trace dc.uba.ar` From the man page:
When tracing is enabled, dig makes iterative queries to resolve the name being looked up. 
It will follow referrals from the root servers, showing the answer from each server that was used to resolve the lookup.

## TIPS

1. If u run `!NUMBER`, this will run command NUMBER from your history
2. Remember that 0, 1 and 2 represent the stdin, stdout and stderr file descriptors respectively
2.1. You can redirect the stderr for example by doing this `find / -name "myfile" 2>/dev/null` <- 
Useful to not show the operation not permitted
3. 
