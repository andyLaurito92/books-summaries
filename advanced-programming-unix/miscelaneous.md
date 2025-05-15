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
