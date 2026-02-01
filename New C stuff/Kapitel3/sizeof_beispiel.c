// Kapitel3/sizeof_beispiel.c

#include <stdio.h>

int main(void){

    int ival = 0;
    double dval = 0;
    printf("sizeof(ival)    : %zu\n", sizeof(ival));    // 4
    printf("sizeof(dval)    : %zu\n", sizeof(dval));    // 8
    // So geht es auch 
    printf("sizeof(float)   : %zu\n", sizeof(float));   // 4
    size_t sz = sizeof(char);
    printf("sizeof(char)    : %zu\n", sz);              // 1

    return 0;
}