// Kapitel5/geheimnummer.c
#include <stdio.h>

int main(void){
    int geheimnummer = 0;
    printf("Geheimnummer eingeben: \n");
    int check = scanf("%d", &geheimnummer);
    if(!check){
        printf("Fehler bei der Eingabe!");
        return 1;
    }
    else if (!(geheimnummer == 12345)){
        printf("Geheimnummer ist falsch!\n");
    }
    else{
        printf("Geheimnummer ist richtig!\n");
    }
    return 0;
}