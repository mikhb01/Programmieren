#include <stdio.h>
#include <string.h>

int main(){

char str1[10] = "Bro";
char str2[] = "Bro";

// strcat(str1, str2);
// printf("%s", str1);


    //strlwr(str1);                                  // converts a string to lowercase
    //strupr(str1);                                  // converts a string to uppercase
    //strcat(str1, str2);                         // appends str2 to end of str1
    //strncat(str1, str2, 1);                    // appends n characters from str2 to str1
    //strcpy(str1, str2);                        // copy str2 to str1
    //strncpy(str1, str2, 4);                    // copy n characters of str2 to str1

    // int result = strlen(str1);
    // printf("%d", result);

    int result = strcmp(str1, str2);

    // printf("%d", result);

    if (result == 0)
    {
        printf("\nThese strings are the same");
    }
    else
    {
        printf("These strings are not the same");

    }

    return 0;
}