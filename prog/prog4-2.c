//ここに自分の名前

//課題4-2
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
    Car head3;

    head3.num = 0; head3.gas = 0;
    head3.next = NULL;
    show_carlist(&head3, "head3 (1)");
    add_car3(&head3, 1357, 40.3);
    add_car3(&head3, 2468, 33.8);
    add_car3(&head3, 3579, 0);
    show_carlist(&head3, "head3 (2)");

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
