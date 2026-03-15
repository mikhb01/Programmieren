//Kapitel6/aufgabe8.c

#include <stdio.h>

int main(void){
    float konto = 0.0, jahre = 0.0;

    printf("Wie viel wollen Sie auf dem Konto einzahlen?: ");
    float check = scanf("%f", &konto);
    if(check != 1){
        printf("Fehler bei der Eingabe...\n");
        return 1;
    }

    printf("Wie viele Jahre wollen Sie einsehen?: ");
    float check2 = scanf("%f", &jahre);
    if(check2 != 1){
        printf("Fehler bei der Eingabe...\n");
        return 1;
    }

    printf("Zinsatz: 2 Prozent\n");
    
    for(int i = 0; i <= jahre; i++){
        printf("Jahr: %d\t\t Kontostand: %.2f\n", i, konto);
        konto *= 1.02;
    }
    printf("Vielen Dank für Ihre Nutzung!\n");
    return 0;
}