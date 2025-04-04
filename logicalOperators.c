#include <stdio.h>
#include <stdbool.h>

int main() {

/*    // logical operators = && (AND) checks if two conditions are true

    float temp = 25;
    bool sunny = false;

    if(temp >= 0 && temp <=30 && sunny == true){
        printf("\nThe weather is good");
    }
    else{
        printf("\nThe weather is bad");
    }
*/
    

/*    // logical operators = || (OR) checks if at least one condition is true
    float temp = 25;
    bool sunny = false;

    if(temp <= 0 || temp >= 30 || sunny == false){
        printf("\nThe weather is bad");
    }
    else{
        printf("\nThe weather is good");
    }
*/

    // logical operators = ! (NOT) reverses the state of a condition

   bool sunny = false;
   
   if(!sunny == true){
    printf("\nIt's cloudy outside");
   }
   else{
    printf("\nIt's sunny outside");
   }


return 0;
}