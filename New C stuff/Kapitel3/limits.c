// Kapitel3/limits.c

#include <stdio.h>
#include <limits.h>

int main(void){

    printf("min. char-Wert          : %d\n",SCHAR_MIN);         // -128
    printf("max. char-Wert          : +%d\n",SCHAR_MAX);        // +128
    printf("min. short-Wert         : %d\n",SHRT_MIN);          // -32768
    printf("max. short-Wert          : +%d\n",SHRT_MAX);         // +32767
    printf("min. int-Wert           : %d\n",INT_MIN);           // -2147483648
    printf("max. int-Wert           : +%d\n",INT_MAX);          // +2147483647
    printf("min. long-Wert          : %ld\n",LONG_MIN);         // -2147483648
    printf("max. long-Wert          : +%ld\n",LONG_MAX);        // +2147483647
    printf("min. long long-Wert     : %lld\n",LONG_LONG_MIN);   // -9223372036854775808
    printf("max. long long-Wert     : +%lld\n",LONG_LONG_MAX);  // +9223372036854775807


    return 0;
}