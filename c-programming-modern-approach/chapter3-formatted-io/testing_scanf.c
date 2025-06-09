#include <stdio.h>


// function has to be defined before used
void using_scanf(void) {
  int x, y;
  float m, h;

  // You can pass multiple converstion specifications! scanf knows how to read
  // multiple values at the same time
  scanf("%d%d%f%f", &x, &y, &m, &h);

  printf("%d %d %1.2f %1.2f receieved", x, y, m, h);

  // Be aware of not referentiating the value of the variable!
  //scanf("%d", x);

  // It can produces a segmentation fault!
  //printf("%d received", x); - segmentation fault

  // We can read by using format strings that contain things that
  // are not convertion specification. Characters (for ex /) will
  // be used to match in the input. Ex of valid input: 3/ 2
  scanf("%d/ %d", &x, &y);
  printf("%d %d", x, y);
}

void reading_from_stdin(void) {
  // TODO
}

/*
 * Instead of using scanf, is better to read characters
 * from stdin and then convert them to what you expect.
 * In this way, we can handle errors on receiveing
 * unexpected types
 */

int main(void) {
  using_scanf();
  return 0;
}
