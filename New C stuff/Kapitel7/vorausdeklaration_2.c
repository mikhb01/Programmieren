//Kapitel7/vordeklaration_2.c

#include <stdio.h>

void hallo(void);   //Funktionsprototyp

int main(void){
    printf("Vor der Funktion\n");
    hallo();
    printf("Nach der Funktion\n");
    return 0;
}

void hallo(void){
    printf("In der Funktion\n");
}

