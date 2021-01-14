#include <stdio.h>

int sum();

int main(void)
{
    int num1 = 5;
    int num2 = 5;
    int result = sum(num1, num2);
    printf("hola\n");
    printf("%i",result);
}

int sum(int x, int y)
{
    return x + y;
}