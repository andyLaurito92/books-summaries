#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void reverse_array(char* arr) {
  size_t len = strlen(arr);

  printf("Size of digit is %zu\n", len);
  
  for(size_t i = 0; i < len / 2; i++) {
    char temp = arr[i];
    arr[i] = arr[len - 1 - i];
    arr[len - 1 - i] = temp;
  }

  printf("Reversed number is: %s\n", arr);
}

void reverse_number1(void) {
  char digits[100];
  
  printf("Insert number\n");
  scanf("%99s", digits);

  reverse_array(digits);
}


/**
 * C doesn't have by default a resizable array, therefore
 * we need to do sht like this :)
 */
void reverse_number_using_resizable_array(void) {

  char *arr = NULL;
  size_t size = 0;      // current number of elements
  size_t capacity = 2;  // initial capacity
  
  arr = malloc(capacity * sizeof(int));
  
  printf("Enter digits (Ctrl+D to end input on Unix, Ctrl+Z on Windows):\n");

  char input;
  while (scanf(" %c", &input) == 1) {
    // Resize if needed
    if (size >= capacity) {
      capacity *= 2;
      arr = realloc(arr, capacity * sizeof(int));
      if (arr == NULL) {
	perror("realloc failed");
	exit(EXIT_FAILURE);
      }
    }
    arr[size++] = input;
  }

  reverse_array(arr);
    
  free(arr);
}


int main(void) {
  printf("Which algorithm do you want to run?\n");
  printf("Choose 1 for fixed array length or 2 for resizable array\n");
  int option;
  scanf("%d", &option);
  if (option == 1) {
    reverse_number1();
  } else if (option == 2) {
    reverse_number_using_resizable_array();
  } else {
    fprintf(stderr, "Value Error: Expected 1 or 2, received %d\n", option);
    exit(EXIT_FAILURE);
  }

  // reverse_number_using_resizable_array();
  return 0;
}
