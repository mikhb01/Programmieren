// Kapitel5/if_beispiel.c

#include <stdio.h>

int main(void){

    int iVal = 0;
    printf("Bitte eine Ganzzahl eingeben: \n");
    int check = scanf("%d", &iVal);
    if(check){
        //Code wird ausgeführt, wenn die Bedingung nicht 0 ist
        printf("Ihre Eingabe: %d\n", iVal);
    }
    printf("Außerhalb der if-Verzeigung\n");
    return 0;
}