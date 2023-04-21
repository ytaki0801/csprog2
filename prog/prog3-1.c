//ここに自分の名前

//課題3-1
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int num, i;
    int *array;
    /* int型の配列を作る処理 */
    printf("num > ");
    scanf("%d", &num);

    /* 以降に課題3-1の処理を追記する */



    /* 配列の要素を出力する */
    for(i=0; i<num; i++) {
        printf("%d ", *(array+i));
    }
    printf("\n");
    /* 不要になったメモリを解放する */
    free(array);

    return 0;
}
