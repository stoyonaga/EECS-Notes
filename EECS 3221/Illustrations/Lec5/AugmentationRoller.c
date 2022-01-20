#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(){
    int i;
    int n = 1;
    int pid = fork();
    if (pid != 0){
        n = 6;
        wait();
    }
    for (i = 0; i < 5; i++){
        printf("%d ", n);
        n += 1;
    }
    printf("\n");
    return 0;
}
