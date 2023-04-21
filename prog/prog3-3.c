//ここに自分の名前

//課題3-3
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    int *array;

    printf("---make_even(7)---\n");
    array = make_even(7);
    for(i=0; i<7; i++) {
        printf("%d ", *(array+i));
    }
    printf("\n");
    free(array);
    printf("---make_even(10)---\n");
    array = make_even(10);
    for(i=0; i<10; i++) {
        printf("%d ", *(array+i));
    }
    printf("\n");
    free(array);

    return 0;
}
