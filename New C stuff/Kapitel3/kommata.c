// Kapitel3/kommata.c

#include <stdio.h>
#include <wchar.h>
#include <complex.h>

int main(void){

    float fVal = 3.33f;
    long double  ldVal = 32.321;
    double eVal = 3.2e10;
    double eVal2 = 3.4e-5;
    long double eVal3 = 8.4e-123;

    printf("%f\n", fVal);
    printf("%Lf\n", ldVal);
    printf("%f\n", eVal);
    printf("%f\n", eVal2);
    printf("%Lf\n", eVal3);

    // float _Complex;
    // double _Complex;
    // long double _Complex;

    // float complex;
    // double complex;
    // long double complex;
    
    return 0;
}