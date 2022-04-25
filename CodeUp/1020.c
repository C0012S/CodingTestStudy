#include <stdio.h>

int main() {
    int number1, number2;
    scanf("%d-%d", &number1, &number2);
    printf("%06d%07d", number1, number2);
    
    return 0;
}