#include <stdio.h>

int main()
{
    int c = 194;
    int a;                     // Declare a variable of type int
    int *p;                    // Declare a pointer variable of type int

    a = 10;                    // Assign the value 10 to a
    p = &a;                    // Assign the address of a to p

    printf("%p\n", p);         // Print the address stored in p
    printf("%d\n", *p);        // Print the value stored in the address stored in p         
    printf("%p\n", &a);        // Print the address of a

    int b = 40;               // Declare a variable of type int
    *p = b;                   // Assign the value 40 to the address stored in p

    printf("%p\n", p);
    printf("%d\n", *p);

    printf("%p\n", p + 1);

    printf("%d\n", *(p + 1));
    printf("%d\n", *p + 1);

    printf("%d\n", *(p - 1));
    printf("%d\n", *p - 1);


    return 0;
}