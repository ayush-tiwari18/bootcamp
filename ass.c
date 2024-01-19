#include<stdio.h>
// #define num=10;
int main()
{
    char name[10];
    char course[10];

    for(int i=0 ; i<10 ; i++){
        scanf("%c",&name);
        // scanf("%c",&course);
    }
    for(int i=0 ; i<10 ; i++){
        scanf("%c",&course);
        // scanf("%c",&course);
    }

    if(course == "python")
    printf("Hello %s, you are in python class.",name);
    return 0;
}