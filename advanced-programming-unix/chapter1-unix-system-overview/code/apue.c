#include "apue.h"
#include <errno.h>	/* for definition of errno */
#include <stdarg.h>	/* ISO C variable arguments */

static int err_doit(int, int, const char *, va_list) {
  return 0;
}

/**
 * Nonfatal error related to a system call
 * Print a message and return.
 */
void err_ret(const char *fmt, ...) {
  va_list ap;
  va_start(ap, fmt);
  err_doit(1, errno, fmt, ap);
  va_end(ap);
}

/**
   Fatal error unrelated to a system call.
   Print a message and terminate
**/
void err_quit(const char *fmt, ...) {
  va_list ap;

  va_start(ap, fmt);
  err_doit(0, 0, fmt, ap);
  va_end(ap);
  exit(1);
}

/**
 *
 *
 */
void err_sys(const char *fmt, ...) {
  va_list ap;

  va_start(ap, fmt);
  err_doit(1, errno, fmt, ap);
  va_end(ap);
  exit(1);
}
 
