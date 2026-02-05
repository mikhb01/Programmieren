// Kapitel4/kreisberechnung.c

#include <stdio.h>

int main(void){
    const double pi = 3.14159265358979;
    double r = 0.0;
    printf("Radius eingeben: ");
    int check = scanf("%lf", &r);
    if(check != 1){
        printf("Fehler beim Einlesen...\n");
        return 1;
    }
    double aKreis = r * r * pi;
    printf("Kreisflaeche betraegt: %lf\n", aKreis);
    return 0;
}