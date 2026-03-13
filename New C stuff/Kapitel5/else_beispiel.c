// Kapitel 5/else_beispiel.c

#include <stdio.h>

int main(void){

    int iVal = 0;
    printf("Bitte gebe eine Ganzzahl ein: \n");
    int check = scanf("%d", &iVal);
    if(check == 1){
        printf("Ihr Eingabe: %d\n", iVal);
    }
    else{
        printf("Fehler bei der Eingabe \n");
    }
    printf("Außerhalb der if-Verzweigung\n");
    return 0;
}