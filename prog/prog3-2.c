//ここに自分の名前

//課題3-2
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *mystr;

    /* make_string()の動作確認 */
    mystr = make_string();
    printf("mystr: %s\n", mystr);
    free(mystr);

    return 0;
}
