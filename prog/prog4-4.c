//ここに自分の名前

//課題4-4
#include <stdio.h>
#include <stdlib.h>

typedef struct Car {
    int num;
    double gas;
    struct Car *next;
} Car;

int main(void)
{
    Car head5;

    head5.num = 0; head5.gas = 0;
    head5.next = NULL;
    add_car2(&head5, 1357, 40.3);
    add_car2(&head5, 2468, 33.8);
    printf("平均値(1): %lf\n", average_gas(&head5));
    add_car2(&head5, 3579, 26.1);
    printf("平均値(2): %lf\n", average_gas(&head5));

    return 0;
}
