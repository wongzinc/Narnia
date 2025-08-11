#include <unistd.h>

int main() {
    char filename[] = "/bin/sh\x00"
    char **argv, **envp;
    argv[0] = filename;
    argv[1] = 0;
    envp[0] = 0;
    execve(filename, argv,envp);
}