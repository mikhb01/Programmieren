// Kapitel5/elseif_beispiel.c

#include <stdio.h>
int main(void){
    int ival = 0;
    printf("Bitte gebe eine positive Ganzzahl ein: \n");
    int check = scanf("%d", &ival);
    if(check != 1){
        printf("Fehler bei der Eingabe...\n");
    }
    else if (ival <0){
        printf("Keine Negativen Werte oder \"0\" verwenden!\n");
    }
    else {
        printf("Ihre Eingabe: %d\n", ival);
    }
    printf("Außerhalb der if-Verzweigung");
    return 0;
}