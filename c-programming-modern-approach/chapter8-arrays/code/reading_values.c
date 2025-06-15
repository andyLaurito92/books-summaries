#include <stdio.h>
#include <stdlib.h>

#define N 10

int main(void) {
  printf("Enter %d elements to calculate a random average\n", N);
  int a[N];
  for (int i = 0; i < N; i++) {
    scanf("%d", &a[i]);
  }

  int n1 = rand() % N;
  int n2 = rand() % N;

  printf("Average between %d and %d is %f\n", a[n1], a[n2], (a[n1] + a[n2])/2.0);
}
