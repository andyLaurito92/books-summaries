## Loops in C

3 loops: while, for and do. Remember that:
- The while condition is tested *before* executing the body of the loop
- The do condition is tested *after* executing the body of the loop

```
i = 10
do {
	printf("Decrementing i until 0, now: %d", i);
	i --;
} while (i >= 0);
``` 

## for loop

You can ommit expressions in the for loop. Example:

```
int i = 10;
for (; i > 0; i--) {
  printf("Decrementing i: %d\n", i);
}
```

Since i is initialized outside the for, you can ommit the initializaiton in the first for expression.

### C99

Since C99, you can declare a variable in the first for expression:

```
for (int i = 0; i < 10; i++) {
	// do sht
}
```

### Comma expression in for

You can use a , in either the first or third expression of a for statement to either initialize more than 1 variable or
perform more than 1 action over a variable:
