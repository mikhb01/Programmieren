// Kapitel3/float_digits.c

#include <stdio.h>
#include <float.h>

int main(void){


    int i = 0x90AF;

    printf("float Genauigkeit       :%d\n", FLT_DIG);       // 6
    printf("double Genauigkeit      :%d\n", DBL_DIG);       // 15
    printf("long double Genauigkeit :%d\n", LDBL_DIG);      // 18 (im Buch und Cookie: 15)

    printf("%d\n", i);

    return 0;
}