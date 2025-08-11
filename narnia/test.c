#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int (*fp)(char *) = (int(*)(char *))&puts;
    // printf("%lu",((unsigned long)fp & 0xff000000));
    printf("%llx\n",fp);
    printf("%llu", ((unsigned long long)fp & 0xff000000));
    return 0;
}