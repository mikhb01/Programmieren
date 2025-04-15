#include <stdio.h>

int main(){

    char operator;
    double num1;
    double num2;
    double result;

    printf("\nWhat kind of operation do you want to do? (+ - * /)");
    scanf("%c", &operator);

/*    if (operator == '+')
    {
        printf("\nPlease add the numbers you want to add.");
        printf("\nFirst Number: ");
        scanf("%lf", &num1);
        printf("\nSecond Number: ");
        scanf("%lf", &num2);

        result = num1 + num2;

        printf("\nThe result of the addition is: %.2f", result);
    }
    else if (operator == '-')
    {
        printf("\nPlease add the numbers you want to subtract.");
        printf("\nFirst Number: ");
        scanf("%lf", &num1);
        printf("\nSecond Number: ");
        scanf("%lf", &num2);

        result = num1 - num2;

        printf("\nThe result of the subtraction is: %.2f", result);
    }
    else if (operator == '*')
    {
        printf("\nPlease add the numbers you want to multiply.");
        printf("\nFirst Number: ");
        scanf("%lf", &num1);
        printf("\nSecond Number: ");
        scanf("%lf", &num2);

        result = num1 * num2;

        printf("\nThe result of the multiplication is: %.2f", result);
    }
    else if (operator == '/')
    {
        printf("\nPlease add the numbers you want to devide.");
        printf("\nFirst Number: ");
        scanf("%lf", &num1);
        printf("\nSecond Number: ");
        scanf("%lf", &num2);

        result = num1 / num2;

        printf("\nThe result of the devision is: %.2f", result);
    }
    else
    {
        printf("\nPlease enter one of the four operators!");
    }
*/    

    printf("\nEnter number 1: ");
    scanf("%lf", &num1);

    printf("\nEnter number 2: ");
    scanf("%lf", &num2);

    switch (operator)
    {
    case '+':
        result = num1 + num2;
        printf("\nThe result is: %.2lf", result);
        break;
    case '-':
        result = num1 - num2;
        printf("\nThe result is: %.2lf", result);
        break;
    case '*':
        result = num1 * num2;
        printf("\nThe result is: %.2lf", result);
        break;
    case '/':
        result = num1 / num2;
        printf("\nThe result is: %.2lf", result);   
        break;
    default:
        printf("\n%c is not valid", operator);
    }


    return 0;
}