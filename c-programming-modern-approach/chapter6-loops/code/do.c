#include <stdio.h>

int main(void) {
  int i = 10;
  do {
    printf("Decrementing i until 0, now: %d\n", i);
    i --;
  } while (i >= 0);
}
