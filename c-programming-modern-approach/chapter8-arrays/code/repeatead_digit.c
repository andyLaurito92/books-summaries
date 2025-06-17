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
}
