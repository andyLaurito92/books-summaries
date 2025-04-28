#include "apue.h"
#include <sys/wait.h>

int main(void) {
  char buf[MAXLINE];
  pid_t pid;
  int status;

  printf("%% "); // print prompt
  while (fgets(buf, MAXLINE, stdin) != NULL) {
    if (buf[strlen(buf) - 1] == '\n')
      buf[strlen(buf) - 1] == 0;

    if ((pid = fork()) < 0) {
      // Returns non-negative integer to the parent
      // This value is the PID of the child
      err_sys("fork error");
    } else if (pid == 0) {
      /* child */
      execlp(buf, buf, (char *)0); //Spawn a process that executes the command
      err_ret("couldn't execute: %s", buf);
      exit(127);
    }

    /* parent */
    if ((pid = waitpid(pid, &status, 0)) < 0)
      // waitpid also returns the termination status in &status
      err_sys("waitpid error");
    printf("%% ");
  }
  exit(0);
}
