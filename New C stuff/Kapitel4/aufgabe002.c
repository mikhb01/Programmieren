// Kapitel4/aufgabe002.c

#include <stdio.h>

int main(void){

    double TC = 0;
    double TK = 0;
    double TF = 0;

    printf("Geben Sie eine Temperatur in Grad Celcius an: ");
    int check = scanf("%lf", &TC);
    if (check != 1){
        printf("Fehler bei scanf...\n");
        return 1;   //Programm beenden
    }
    // TF = ((TC * 9)/5) + 32
    // TK = TC + 273.15
    TF = ((TC * 9)/5) + 32;
    TK = TC + 273.15;
    printf("%.2lf in Grad Celius betragen %.2lf in Grad Fahrenheit\n", TC, TF);
    printf("%.2lf in Grad Celius betragen %.2lf Kelvin\n", TC, TK);
    return 0;
}