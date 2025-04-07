#include <stdio.h>

enum Day{Sun = 7, Mon = 1, Tue = 2, Wed = 3, Thu = 4, Fri = 5, Sat = 6};

int main()
{
    // enum = a user defined type of named integer identifiers
    //          helps to make a program more readable

    enum Day today = Mon;

    printf("%d\n", today); // enums are NOT STRINGS, but they can be treated as int

    if(today == Sat || today == Sun)
    {
        printf("It's weekend! Party time!\n");
    }
    else
    {
        printf("I have to work today\n");
    }

    return 0;
}