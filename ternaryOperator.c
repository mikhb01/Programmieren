#include <stdio.h>

int findMax(int x, int y){
    return (x > y) ? x : y;
}

int main(){

    // ternary operation = shortcut to if/else when assigning/returning a value
    // (condition) ? value if true : value if false

    int max = findMax(5, 4);

    printf("%d", max);

    return 0;
}