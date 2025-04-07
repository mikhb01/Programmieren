#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    const int MIN = 1;
    const int MAX = 100;
    int guess;
    int guesses;
    int answer;
    
    //uses the current time as a seed
    srand(time(0)); 
    
    //generate random number between MIN and MAX
    answer = (rand() % MAX) + MIN; 

    do
    {
        printf("Enter a guess!\n");
        scanf("%d", &guess);
        if (guess > answer)
        {
            printf("\nToo high\n");
        }
        else if(guess < answer)
        {
            printf("\nToo low\n");
        }
        else
        {
            printf("\nCorrect\n");
        }
        guesses++;
    } while (guess != answer);
    

    printf("\nanswer: %d", answer);
    printf("\nguesses: %d", guesses);

    return 0;
}