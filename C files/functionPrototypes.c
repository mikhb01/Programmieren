#include <stdio.h>

void hello(char[], int);

int main(){

    // function prototype

    // WHAT IS IT?
    // Function declaration, w/o a body before main()
    // Ensures that calls to a function are made with the correct arguments
    char name[] = "Leon";
    int age = 23;

    hello(name, age);

    return 0;
}

void hello(char name[], int age){

    printf("\nHello %s!", name);
    printf("\nYou are %d years old!", age);
}