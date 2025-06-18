#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a[100];

  char input;
  int size = 0;

  printf("Enter digits (Ctrl+d to end input)\n");
  while (scanf(" %c", &input) == 1) {
    a[size++] = atoi(&input);
  }

  // No prebuilt hashmap, therefore let's do the naive approach
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      if (a[i] == a[j]) {
	printf("Repeated digit %d\n", a[i]);
      }
    }
  }

  // We are considering digits! There are between 0 & 9
  printf("Faster solution: Digits are between 0 and 9\n");
  int seen[10] = {0};
  for (int i = 0; i < size; i++) {
    if (seen[a[i]] == 0) {
      seen[a[i]] = 1; // If you don't want the message to be repeated per each repetitino, set = 2
    } else {
      printf("Digit %d already seen\n", a[i]);
    }
  }

  // What if the number is already an integer?
  int x = 13153123;
  printf("Repeated digits in %d\n. Using count digits", x);
  int seen2[10] = {0};
  while (x > 0) {
    int digit = x % 10;
    seen2[digit] == 1? printf("Digit %d seen\n", digit) : seen2[digit]++;
    x = (int) x / 10;
  }

  // Instead of using an array, we can directly use bit operations
  x = 1425135124;
  printf("Repeated digits in %d\n: Uisng bitwise operations", x);
  int mask = 0;
  while (x > 0) {
    int digit = x % 10;
    x = (int) x / 10;
    int bit = 1 << digit; // Equivalent to 1*2^digit. This sets the bit of digit to 1

    if (mask & bit) { // Only happens if in the bit that represents the digit in the mask we already have a 1
      printf("Repeated digit %d\n", digit);
    } else {
      mask |= bit; // update mask with seen digit
    }
  }
}
