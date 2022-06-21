#include <stdio.h>

int main() {
    int num1, num2;
    
    scanf("%d %d", &num1, &num2);
    printf("%d", (!num1) && (!num2)); 
    //printf("%d", (num1 == 0) && (num2 == 0));
    
    return 0;
}