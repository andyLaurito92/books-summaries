#include <stdio.h>

int main(void) {
  int integer = 3;
  float afloat = 8.9754;

  // What happens if we invert the convertion specification values?
  printf("%d and %.3f\n", afloat, integer);

  // The value is not well interpreted but eitherway we get a warning error while compiling

  printf("%10.1f", afloat); // prints         9.0
}

