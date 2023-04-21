#include <stdio.h>

typedef struct Car {
    int num;
    double gas;
    struct Car *next;
} Car;

void show_carlist(Car *start, char *str);

int main(void)
{
    Car car0, car1, car2, car3, car4;
    Car *pcar;

    car0.num = 1234; car0.gas = 25.5;
    car1.num = 4567; car1.gas = 52.2;
    car2.num = 7890; car2.gas = 20.5;

    car0.next = &car1;
    car1.next = &car2;
    car2.next = NULL;
    for(pcar = &car0; pcar!=NULL; pcar = pcar->next) {
        printf("num: %d, gas: %lf\n", pcar->num, pcar->gas);
    }
    show_carlist(&car0, "car list");
    show_carlist(&car1, "from car1");

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
