#include <stdio.h>
#include <string.h>

int main()
{
    // for loop = repeats a section of code a limited amount of times

/*   for(int i = 10; i >= 1; i--)
    {
        printf("%d\n", i);
    }*/ 

    // while loop = repeats a section of code possibly unlimited time.
    // WHILE some condition remains true
    // a while loop might not execute at all

  /*  char name[25];
    printf("\nWhat is your name?");
    fgets(name, 25, stdin);
    name[strlen(name)-1] = '\0';

    while(strlen(name) == 0)
    {
        printf("You did not enter your name!");
        printf("\nWhat is your name?");
        fgets(name, 25, stdin);
        name[strlen(name)-1] = '\0';
    }
    

    printf("Hello %s", name);
*/
  
    // while loop = checks a condition, THEN executes a block of code if the condition is true
    // do while loop = always executes a block of code once, THEN checks a condition

    int num = 0;
    int sum = 0;

    do
    {
        printf("Enter a number above 0!");
        scanf("%d", &num);
        if(num > 0)
        {
            sum += num;
        }
    }while(num > 0);


    printf("%d", sum);

    return 0;
}