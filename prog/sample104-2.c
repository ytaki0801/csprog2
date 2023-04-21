#include <stdio.h>
#include <stdlib.h>

typedef struct Car {
    int num;
    double gas;
    struct Car *next;
} Car;

void show_carlist(Car *start, char *str);
void add_car(Car *p);

int main(void)
{
    Car head;
    Car *new;

    head.num = 0; head.gas = 0;
    head.next = NULL;

    show_carlist(&head, "head (1)");

    new = (Car *)malloc(sizeof(Car));
    new->num = 1234; new->gas = 25.5;
    new->next = head.next;

    head.next = new;
    
    show_carlist(&head, "head (2)");

    add_car(&head);
    show_carlist(&head, "head (3)");
    add_car(&head);
    show_carlist(&head, "head (4)");

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

void add_car(Car *p)
{
    Car *new;

    new = (Car *)malloc(sizeof(Car));
    new->num = 1111; new->gas = 11.1;
    new->next = p->next;
    p->next = new;
}
