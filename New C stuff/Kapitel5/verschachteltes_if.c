// Kapitel5/verschachteltes_if.c

#include <stdio.h>

int main (void){
    int ival = 0;
    printf("Bitte eine positve Ganzzahl eingeben: \n");
    int check = scanf("%d", &ival);
    if(check == 1){
        if(ival <0){
            printf("Keine negativen Werte oder \"0\" verwenden\n");
        }
        else {
            printf("Ihre Eingabe: %d\n", ival);
        }
    }
    else {
        printf("Fehler bei der Eingabe!\n");
    }
    printf("Außerhalb der if-Verzweigung");
    return 0;
}