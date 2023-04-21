//ここに自分の名前

//課題4-1
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
    Car head2;

    head2.num = 0; head2.gas = 0;
    head2.next = NULL;
    show_carlist(&head2, "head2 (1)");
    add_car2(&head2, 1357, 40.3);
    add_car2(&head2, 2468, 33.8);
    add_car2(&head2, 3579, 26.1);
    show_carlist(&head2, "head2 (2)");

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
