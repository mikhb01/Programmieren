#include <stdio.h>
#include <string.h>

int main()
{

  /*  // array = a data structure that can store many values of the same data type.

    // double price[] = {5.0, 10.0, 15.0, 25.0, 20.0}; //declaring at init
    // double price[10] = {5.0, 10.0, 15.0, 25.0, 20.0}; //declaring 5 at init and 5 remain unused

    double price[5];

    price[0] = 5.0;
    price[1] = 10.0;
    price[2] = 15.0;
    price[3] = 25.0;
    price[4] = 20.0;


    printf("$%.2lf", price[0]);
*/

    // print array with a loop

/*    double price[] = {5.0, 10.0, 15.0, 25.0, 20.0};


  example 1
    for(int i = 0; i < 5; i++)
    {
        printf("$%.2lf\n", price[i]);
    }
   

    // für arrays, wo man die größe nicht weiß vorher
    for(int i = 0; i < sizeof(price)/sizeof(price[0]); i++)
    {
        printf("$%.2lf\n", price[i]);
    }
*/

/*
    // 2D array = an array, where each element is an entire array
    //             useful if you need a matrix, grid, or table of data
    
    int numbers[2][3] = {
                        {1, 2, 3},
                        {4, 5, 6}
                        };
    

    int numbers[3][3];
    int rows = sizeof(numbers)/sizeof(numbers[0]);
    int columns = sizeof(numbers[0])/sizeof(numbers[0][0]);

    printf("rows: %d\n", rows);
    printf("columns: %d\n", columns);



    numbers[0][0] = 1;
    numbers[0][1] = 2;
    numbers[0][2] = 3;
    numbers[1][0] = 4;
    numbers[1][1] = 5;
    numbers[1][2] = 6;
    numbers[2][0] = 7;
    numbers[2][1] = 8;
    numbers[2][2] = 9;

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            printf("%d ", numbers[i][j]);
        }
        printf("\n");
    }

    */

    // array of strings

    char cars[][10] = {"Mustang", "Corvette", "Camaro"};

    //cars[0] = "Tesla";
    strcpy(cars[0], "Tesla");

    for(int i = 0; i < sizeof(cars)/sizeof(cars[0]); i++)
    {
        printf("%s\n", cars[i]);
    }

    


    return 0;
}