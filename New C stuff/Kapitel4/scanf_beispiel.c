// Kapitel4//scanf_beispiel.c

#include <stdio.h>

int main(void){

    int iVar = 0;
    printf("Bitte eine Ganzzahl eingeben: ");
    int check = scanf("%d", &iVar);
    if(check == EOF) {
        printf("Fehler bei scanf...\n");
        return 1; // Programm beenden
    }
    if(check != 1){
        printf("Fehler bei der Eingabe\n");
        return 1;
    }
    printf("%d Werte eingelesen: ", check);
    printf("der eingegebene Wert lautet: %d\n", iVar);
    printf("Die Adresse von iVar lautet: %p\n", &iVar);

    return 0;
}