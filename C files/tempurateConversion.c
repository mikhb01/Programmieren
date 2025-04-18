#include <stdio.h>
#include <ctype.h>

int main(){

    char unit;
    float temp;

    printf("\nIs the temperature in (F) or (C)?: ");
    scanf("%c", &unit);

    unit = toupper(unit);

    if (unit == 'C')
    {
        printf("\nThe current temperature is in C");
        printf("\nEnter the temperature in Celsius: ");
        scanf("%f", &temp);
        temp = (temp * 9 / 5) + 32;
        printf("\nThe temp in Fahrenheit is: %.1f",temp);
    }
    else if (unit == 'F')
    {
        printf("\nThe current temperature is in F");
        printf("\nEnter the temperature in Fahrenheit: ");
        scanf("%f", &temp);
        temp = ((temp -32) * 5) / 9;
        printf("\nThe temp in Celsius is: %.1f",temp);
    }
    else{
        printf("\n %c is not a valid unit of measurement", unit);
    }
    

    return 0;
}