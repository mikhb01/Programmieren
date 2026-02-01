// Kapitel3//fixed_ints.c

#include <stdio.h>
#include <stdint.h>

int main(void){
    int64_t bigVar = 12345678;
    printf("bigVar          : %lld\n", bigVar);         // 12345678
    printf("sizeof(int64_t) : %zu\n", sizeof(int64_t)); // 8
    printf("INT64_MAX       : %lld\n", INT64_MAX);      // 9223372036854775807

    return 0;
}