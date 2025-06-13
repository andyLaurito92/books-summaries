#include <string.h>
#include <stdio.h>

int main(void) {
  char mystr[100];

  printf("Introduce word:");
  // This only reads words. If a space is introduced it breaks
  // Use fgets instead if you want to read a whole line
  scanf("%99s", mystr); 

  int n = strlen(mystr);
  for (int i = 0, j = n - 1; i < j; i++, j--) {
    if (mystr[i] != mystr[j]) {
      printf("Not a palindrome\n");
      return 0;
    }
  }
  printf("%s is a palindrome\n", mystr);
}
