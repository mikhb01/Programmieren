// Kapitel3/kapitel003.c

#include <stdio.h>


/*
int form1(){
    signed char cVal = 100;
    short sVal = 10000;
    int iVal = 123456;
    long lVal = 123456;
    long long llVal = 123456;

    // unsigned int uVal = 1000u;
    // long lVal = 100000L;
    // unsigned long ulVal = 2222222UL;
    // long long llVal = 1234LL;
    // unsigned long long ullVal = 12341234323ULL;
    unsigned int uHexVal = 0X42U;

    printf("%hhd\n", cVal);
    printf("%hd\n", sVal);
    printf("%d\n", iVal);
    printf("%ld\n", lVal);
    printf("%lld\n", llVal);
    printf("%u\n", uHexVal);
    return 0;
}

int form2(){
    //richtige schreibweise
    typedef unsigned char byte;
    byte MyMem[0x100000];

    // falsche Schreibweise:
    //unsigned char MyMem[0x100000];
}
*/
int main(void){
    // form1();

    char ch = 'A';
    printf("%hhd\n", ch);

    char ch2 = 65;
    printf("%hhd\n", ch2);
}