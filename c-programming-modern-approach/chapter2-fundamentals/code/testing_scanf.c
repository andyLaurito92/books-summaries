#include <stdio.h>

int main(void) {
  int x, y;
  float m, h;

  // You can pass multiple converstion specifications! scanf knows how to read
  // multiple values at the same time
  scanf("%d%d%f%f", &x, &y, &m, &h);

  printf("%d %d %1.2f %1.2f receieved", x, y, m, h);
}
