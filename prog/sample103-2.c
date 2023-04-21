#include <stdio.h>

void show_range(int *ptr, int s, int e);

void show_range(int *ptr, int s, int e)
{
    int i;
    for(i=s; i<=e; i++) {
        printf("*ptr+%d: %d, ptr+%d: %p\n", i, *(ptr+i), i, ptr+i);
    }
}

int main(void)
{
    int test[5] = {80, 60, 55, 22, 75};
    printf("---show_range(test, 2, 4)---\n");
    show_range(test, 2, 4);
    printf("---show_range(test, 1, 3)---\n");
    show_range(test, 1, 3);
    return 0;
}
