#include <stdio.h>

int main(void) {
  // We can initialize arrays in-line as this
  char a[10] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};
  int b = 42;

  for (int i = 0; i < 20; i++) {
    a[i] = 'A'; // Intentionally overflow
  }
  
  printf("b = %d\n", b); // Should not be 42 anymore
  return 0;
}
