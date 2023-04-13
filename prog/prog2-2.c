/* ここに自分の名前を入れる */
#include <stdio.h>

/* 関数のプロトタイプ宣言 */
int sum_range(int *ptr, int s, int e);

int main(void)
{
    int test[5] = {80, 60, 55, 22, 75};
    int test2[5] = {76, 85, 47, 92, 68};

    printf("sum_range: %d\n", sum_range(test, 1, 3));
    printf("sum_range: %d\n", sum_range(test2, 2, 4));

    return 0;
}

int sum_range(int *ptr, int s, int e)
{

}
