#include <stdio.h>


Create a C function that receives to strings and appends them and outputs them in stdout

 Here's a simple C function that concatenates two strings and prints the result:

```c
void concatAndPrint(char* str1, char* str2) {
    char *concatenated = malloc((strlen(str1) + strlen(str2)) * sizeof(char));
    strcpy(concatenated, str1);
    strcat(concatenated, str2);
    printf("%s\n", concatenated);
    free(concatenated);
}
```

In this function, we first allocate memory for the combined string and copy `str1` into it. Then, we append `str2` to the end of the combined string using the `strcat()` function. Finally, we print the result and free the allocated memory. This function can be used in a larger C program as desired.

int main() {
  int x = 1;
  printf("%d\n", ++x); // prints 2
  printf("%d\n", x++); // prints 2 and then executes +=1
}


Create a c function that receives two integers and returns its sum

 ```c
int sum(int a, int b) {
    return a + b;
}
```

