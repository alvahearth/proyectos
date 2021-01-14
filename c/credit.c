#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int num = 1234;

    int num2 = num / 10;
    int lastDigit = num % 10;
    printf("%i\n",lastDigit);
    printf("%i\n",num2);
    
}
