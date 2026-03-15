//Kapitel5/oder_operator.c

#include <stdio.h>

int main(void){
    unsigned int uval1 = 0, uval2 = 0;
    printf("Bitte 2 Ganzzahlen eingeben: \n");
    int check = scanf("%u %u", &uval1, &uval2);
    if(check != 2){
        printf("Fehler bei der Eingabe!\n");
    }
    if ((!uval1)||(!uval2)){
        printf("Fehler: Einer der Werte ist gleich 0\n");
    }
    else {
        printf("%u / %u = %lf\n", uval1, uval2, (double)uval1/uval2);
    }
    return 0;
}