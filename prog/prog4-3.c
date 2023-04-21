//ここに自分の名前

//課題4-3
#include <stdio.h>
#include <stdlib.h>

typedef struct Car {
    int num;
    double gas;
    struct Car *next;
} Car;

void show_carlist(Car *start, char *str);


int main(void)
{
    Car head4;

    head4.num = 0; head4.gas = 0;
    head4.next = NULL;
    add_car2(&head4, 1357, 40.3);
    add_car2(&head4, 2468, 33.8);
    show_greater(&head4, 2467);
    add_car2(&head4, 3579, 26.1);
    show_greater(&head4, 2467);

    return 0;
}

void show_carlist(Car *start, char *str)
{
    Car *pcar;
    printf("--- %s ---\n", str);
    for(pcar = start; pcar!=NULL; pcar = pcar->next) {
        printf("num: %d, gas: %lf\n", pcar->num, pcar->gas);
    }
}
