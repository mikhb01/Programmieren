//Kapitel5/und_operator.c

#include <stdio.h>

int main(void){
    int ival = 0;
    printf("EIne Zahl von 1 bis 10 eingeben: \n");
    int check = scanf("%d", &ival);
    if(check != 1){

        printf("Fehler bei der Einagbe!\n");
        return 1;
    }
    if((ival > 0 ) && (ival <= 10)){
        printf("Zahl ist zwischen 1 und 10!\n");
    }
    else{
        printf("Zahl ist nicht zwischen 1 und 10!\n");
    }
    return 0;
}