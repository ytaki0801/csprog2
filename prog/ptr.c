#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *str;
    int num, i;

    printf("num > ");
    scanf("%d", &num);

    str = (char *)malloc(sizeof(char)*(num+1));
    if (str == NULL) {
        printf("not allocated.\n");
        return 1;
    }

    for (i = 0; i < num; i++) {
        *(str+i) = 'a';
    }
    *(str+i) = '\0';
    printf("str: %s\n", str);

    free(str);

    return 0;
}
