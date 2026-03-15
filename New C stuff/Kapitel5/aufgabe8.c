//Kapitel5/aufgabe8.c

#include <stdio.h>

int main(void){

    int ival = 0;
    printf("Bitte geben Sie eine Zahl zwischen 1 und 100 ein: \n");
    int check = scanf("%d", &ival);
    if(check != 1){
        printf("Fehler bei der Eingabe!\n");
        return 1;
    }
    if((ival < 1) || (ival > 100)){
        printf("Die Zahl ist außerhalb des Bereiches 1 - 100!\n");
    }
    else{
        if (ival % 2 == 0){
            printf("Die Zahl %d ist eine gerade Zahl!\n", ival);
        }
        else{
            printf("Die Zahl %d ist eine ungerade Zahl!\n", ival);
        }
    }
    return 0;
}