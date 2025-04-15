#include <stdio.h>
#include <string.h>

int main(){

    char name[25]; //bytes
    int age;

    printf("\nWhats your name?");
    //scanf("%s", &name); // scannt nur bis zum ersten Leerzeichen
    fgets(name, 25, stdin); // scannt die string länge; kreiert automatisch eine neue line; daher wird "#include <string.h>" importiert
    name[strlen(name)-1] = '\0'; // sorgt dafür, dass keine neue line erzeugt wird, sondern in der gleichen zeile weitergeschrieben wird

    printf("\nHow old are you?");
    scanf("%d", &age);

    printf("\nHello %s, how are you?", name);
    printf("\nYou are %d years old", age);


    return 0;
}