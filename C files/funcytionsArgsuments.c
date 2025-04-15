#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void birthday(char x[], int y){

    printf("\nHappy birthday dear %s!", x);
    printf("\nYou are now %d years old!", y);

}

double square(double x){
    //double result = x * x;
    return x * x;

}
int main(){
    double x = square(3.14);
    printf("%lf", x);

    return 0;
}

/*
int main(){

    char name[] = "Bro";
    int age = 21;

    birthday(name, age);


    return 0;
}*/