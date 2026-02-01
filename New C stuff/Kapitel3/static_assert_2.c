// Kapitel3/static_assert_2.c

#include <stdio.h>
#include <assert.h> // für static_assert()
#include <limits.h> // für CHAR_BIT

int main(void){

    static_assert(CHAR_BIT == 8,
                    "unsigned char hat hier nicht 8 Bit!");

    return 0;
}