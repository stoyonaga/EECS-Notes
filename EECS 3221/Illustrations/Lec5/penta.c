#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char * argv[]){
    /*
     *  Extension Challenge: Write a program that creates five processes (Hence, prints "Hello World!\n" five times!) 
     */
    
    int id1 = fork();              // Two Processes are now Running 
    int id2 = fork();              // Four Processes are now Running
            
    if(id1 != 0 && id2 != 0){      // Check for the First (Parent) Process
    fork();
    }
    printf("Hello World!\n");
    return 0;
