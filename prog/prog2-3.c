/* ここに自分の名前を入れる */
#include <stdio.h>

/* 時間を表す構造体 */
typedef struct Time {
    int hour;
    int minute;
} Time;

/* 関数のプロトタイプ宣言 */
void show(Time *t, char *s);

int main(void)
{
    Time t1 = {40, 50};
    Time t2 = {30, 40};

    show(&t1, "t1");
    show(&t2, "t2");

    return 0;
}

void show(Time *t, char *s)
{

}

