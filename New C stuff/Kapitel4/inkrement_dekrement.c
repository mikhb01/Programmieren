// Kapitel4/inkrement_dekrement.c

#include <stdio.h>

int main(void){
    int ival = 1;
    printf("ival: %d\n", ival);
    ival++;
    printf("ival: %d\n", ival);
    printf("ival: %d\n", ival++);
    printf("ival: %d\n", ival);
    printf("ival: %d\n", ++ival);
    int iVar = 5;
    int aVar = iVar + iVar++;
    printf("aVar: %d\n", aVar);

    return 0;
}

