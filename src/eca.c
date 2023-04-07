#include <stdio.h>
#include <stdlib.h>

#define CN 60
#define ST 30

int main(void)
{
  char r[8], c[CN], cn[CN], b, x, y, z;
  int rule = 22;   

  for (b = rule, x = 0; x < 8; x++) { r[x] = b & 0x01 ? 1 : 0; b >>= 1; }
  for (int i = 0; i < CN; i++) c[i] = 0; c[CN/2] = 1;

  system("cls");
  for (int j = 0; j < ST; j++) {
    for (int i = 0; i < CN; i++) printf("%c", c[i] ? '*' : ' ');
    printf("\n");
    for (int i = 0; i < CN; i++) cn[i] = r[(i == 0 ? 0 : c[i-1])*4+c[i]*2+(i == CN-1 ? 0 : c[i+1])];
    for (int i = 0; i < CN; i++) c[i] = cn[i];
  }

  return 0;
}