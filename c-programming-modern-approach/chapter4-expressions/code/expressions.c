#include <stdio.h>


int main() {
  int x = 1;
  printf("%d\n", ++x); // prints 2
  printf("%d\n", x++); // prints 2 and then executes +=1
}
