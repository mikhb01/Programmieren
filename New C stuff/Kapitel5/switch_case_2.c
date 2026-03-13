// Kapitel5/switch_case_2.c

#include <stdio.h>

int main(void){
    int opt = 0;
    printf("-1- Option A\n");
    printf("-2- Option B\n");
    printf("-3- Option C\n");
    printf("-4- Option D\n");
    printf("-5- Option E\n");
    printf("Ihre Auswahl bitte: \n");
    int check = scanf("%d", &opt);
    if(check !=  1){
        printf("Fehler bei der Eingabe...\n");
        return 1;
    }
    switch(opt){
        case 1  :   printf("Option A beinhaltet auch \n");
        case 2  :   printf("Option B\n");
                    break;
        case 3  :  
        case 4  :   printf("Option C und D sind gleich\n");
                    break;
        case 5  :   printf("Level 5 war die Auswahl\n");
                    break;
        default :   printf("%d? Unbekannte Option!\n", opt);
    }
    return 0;
}