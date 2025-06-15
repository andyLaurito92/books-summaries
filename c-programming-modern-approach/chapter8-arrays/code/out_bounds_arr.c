/**
 * Depicting one of the main issues in C: The out of boundary errors
 * This program can eventually not finish if variable int i is stored
 * AFTER the array!
 */
#include <stdio.h>

// In order to show the issue, you will probably need to disable
// the stack protection rule and 0 optimization
// cc -fno-stack-protector -O0 out_bounds_arr.c
int main(void) {
  int a[10], b = 42;
  for (int i = 0; i <= 10; i++)
    a[i] = 0;

  printf("b=%d", b);
}
