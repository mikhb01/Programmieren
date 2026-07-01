#include <stdio.h>
#include <math.h>
#include <mpfr.h>

int main(void){

    mpfr_t x;
    mpfr_init2(x, 4000);

    mpfr_set_d(x, 0.25, MPFR_RNDN);
    mpfr_pow_ui(x, x, 1561, MPFR_RNDN);

    mpfr_printf("%.50Re\n", x);

    mpfr_clear(x);
    return 0;
}