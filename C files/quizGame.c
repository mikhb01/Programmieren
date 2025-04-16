#include <stdio.h>
#include <ctype.h>

int main(){

    char questions[][100] = {"1. Where were you born?: ",
                            "2. What is the Name of your University in german?: ",
                            "3. Who is the german \"Muddi\"?: "};

    char options[][100] = {"A. Aachen", "B. Bremen", "C. Celle", "D. Dortmund",
                            "A. Uni Bremen", "B. FOM Bremen", "C. Hochschule Bremen", "D. Goethe-Institut Berlin",
                            "A. Angela Merkel", "B. Jens Spahn", "C. Joachim Gauck", "D. Ursula von der Leyen"};
    
    char answers[3] = {'B', 'C', 'A'};
    int numberOfQuestions = sizeof(questions)/sizeof(questions[0]);

    char guess;
    int score;

    printf("QUIZ GAME\n");

    for(int i = 0; i < numberOfQuestions; i++)
    {
        printf("%s\n", questions[i]);
        for (int j = (i * 4); j < (i * 4) + 4; j++)
        {
            printf("%s\n", options[j]);
        }
        
        printf("Guess: ");
        scanf("%c", &guess);
        getchar;
        //scanf("%c%*c", &guess);
        //scanf("%c"); //clear \n from input buffer

        //guess = toupper(guess);

        if (guess == answers[i])
        {
            printf("Correct!\n");
            score++;
        }
        else{
            printf("Wrong!\n");
        }
        
    }

    printf("FINAL SCORE: %d/%d", score, numberOfQuestions);
                            
    return 0;
}