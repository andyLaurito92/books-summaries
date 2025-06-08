#include <stdio.h>
#include <strings.h>

#define MESSAGE "Thanks user!\n" // Macro for defining constant

const char* goodbye = "Goodbye user!\n";

int main(void) {
  // Use scanf to scan input from stdin
  int user_input;

  printf("Plz enter an integer\n");
  scanf("%d", &user_input);
  printf("Value is %d\n", user_input);
  printf(MESSAGE);
  printf("%s", goodbye);
}
