#include <stdio.h>

/**
 ** This program won't run because it doesn't has defined the main
 ** function.
 ** This method is looked up by the linker (ld)
 **/
int testing() {
  printf("Does it work if no main defined?");
  return 0;
}
