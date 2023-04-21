//ここに自分の名前

//課題3-4
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *mystr;

    printf("---fill_alpha(5)---\n");
    mystr = fill_alpha(5);
    printf("mystr: %s\n", mystr);
    free(mystr);
    printf("---fill_alpha(20)---\n");
    mystr = fill_alpha(20);
    printf("mystr: %s\n", mystr);
    free(mystr);

    return 0;
}
