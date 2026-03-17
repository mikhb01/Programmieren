//Kapitel7/vordekleration_1.c

#include <stdio.h>

int main(void){
    printf("Vor der Funktion\n");
    hallo();
    printf("Nach der Funktion\n");
    return 0;
}

void hallo(void){
    printf("In der Funktion\n");
}

