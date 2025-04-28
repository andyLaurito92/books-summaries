#include "apue.h"

int main(void) {
  // getpid() returns pid_t data type. This type fits in a long
  printf("hollo world from process ID %ld\n", (long)getpid());
  exit(0);
}
