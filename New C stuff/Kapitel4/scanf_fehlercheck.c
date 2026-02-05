// Kapitel4//scanf_fehlercheck.c

#include <stdio.h>

int main(void){

    int iVar1 = 0, iVar2 = 0;
    printf("Bitte zwei Ganzzahl eingeben: ");
    int check = scanf("%d %d", &iVar1, &iVar2);
    if(check != 2){
        printf("Zwei Ganzzahlen erwartet\n");
        return 1;
    }
    printf("%d Werte eingelesen: ", check);
    printf("%d und %d\n", iVar1, iVar2);

    return 0;
}