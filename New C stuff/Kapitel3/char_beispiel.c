// Kapitel3/char_beispiel.c

#include <stdio.h>
#include <stddef.h>
#include <uchar.h>
#include <wchar.h>

// int uniCode(){

//     char utf8ch = u'Z';        // UTF-8
//     char16_t utf16ch = u'Z';    // UTF-16
//     char32_t utf32ch = U'Z';    // UTF-32

//     printf("%u\n", utf8ch);
//     printf("%u\n", utf16ch);
//     printf("%U\n", utf32ch);
// }

int main(void) {
    uniCode();
}

int asciiChar(){
    char ch01 = 'A';    // bei ASCII 65
    char ch02 = 66;     // besser wäre 'B'
    printf("Dezimal: %d; Zeichen: %c\n", ch01, ch01);
    printf("Dezimal: %d; Zeichen: %c\n", ch02, ch02);

    // wchar_t ch = L'Z';

    // wprintf("%lc\n", ch);
}

