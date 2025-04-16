#include <stdio.h>

int main(){
    // BITWISE OPERATORS = special operators used in bit level programming 
    //                     (knowing binary is important for this topic)
    
    // & = AND
    // | = OR 
    // ^ = XOR 
    // << = left shift
    // >> = right shift

    // 00000000 = 0
    // 00000001 = 1
    // 00000010 = 2
    // 00000100 = 4
    // 00001000 = 8
    // 00010000 = 16
    // 00100000 = 32
    // 01000000 = 64
    // 10000000 = 128

    int x = 6;  //  6 = 00000110
    int y = 12; // 12 = 00001100
    int z = 0;  //  0 = 00000000

    z = x & y;
    printf("AND = %d\n", z); //00000100

    z = x | y;
    printf("OR = %d\n", z); //00001110

    z = x ^ y;
    printf("XOR = %d\n", z); //00001010

    z = x << 1;
    printf("LEFT SHIFT = %d\n", z); //00001100

    z = x >> 1;
    printf("RIGHT SHIFT = %d\n", z); //00000011

    return 0;
}