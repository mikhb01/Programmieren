// Kapitel2/erstes_programm.c
#include <stdio.h>
#include <conio.h> // only available on windows systems

int main(void){
    printf("Mein erstes Programm\n");
    // getch(); // windows 11 waits for a key press
    printf("Ich werde ein \
    Filmstar... \
    oder auch nicht \n");
    printf("Gib mir zehn: %d", 10);
    printf("Gib mir zehn: %d - gib mir fünf: %d\n", 10, 2+3);
    getch();

    printf("Ich bin ein \"Blindtext\"\n");
    printf("\t Noch mehr Text \n");
    printf("Ich werde überschrieben \r");
    printf("Von mir, einem weiteren Blindtext\n");
    printf("Das Leer \bzeichen wird entfernt\n");

    return 0;
}