#ifndef _APUE_H
#define _APUE_H

#include <sys/ioctl.h>

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>


void err_quit(const char *, ...) __attribute__((noreturn));
void err_sys(const char *, ...) __attribute__((noreturn));


#endif /* _APUE_H */
