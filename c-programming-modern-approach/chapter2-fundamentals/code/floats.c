#include <stdio.h>

int main(void) {
  float height = 3.8432f; //Use f when defining constants.
  //printf("Height is %f", height); // By default, %f prints 6 digits
  printf("Height is %.2f", height); // 2 digits
}
