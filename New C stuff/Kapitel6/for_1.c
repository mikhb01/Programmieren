//Kapitel6/for_1.c

#include <stdio.h>

// int main(void){
//     for(int cnt = 1; cnt <= 5; cnt++){
//         printf("%d. Schleifendurchlauf\n", cnt);
//     }
//     return 0;
// }

int main(void){
    for(int cnt = 1; cnt <= 5; printf("%d. Schleifendurchlauf\n", cnt++));
    return 0;
}