#include <stdio.h>

int main() {
    /*
        Pointers: Variables that store the address of another variable.    
    */
    int a;                      // declare a variable of type int
    int *p;                     // declare a pointer variable of type int

    p = &a;                     // assign the address of a to p
    a = 5;                      // assign 5 to a

    //  p -> address
    // *p -> value at address

    printf("%d\n", *p);         // print the value at the address stored in p
    printf("%p\n", p);          // print the address stored in p
    printf("%p\n", &a);         // print the address of a
    printf("%p\n", &p);         // print the address of p

    // dereferencing
    
    *p = 10;                    // assign 10 to the value at the address stored in p
    printf("%d\n", a);          // print the value of a

    return 0;             
} 