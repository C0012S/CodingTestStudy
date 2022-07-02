#include <stdio.h>

int main() {
    char al, temp = 'a';
    
    scanf("%c", &al);
    
    do {
        printf("%c ", temp);
        temp += 1;
    } while (temp <= al);
    
    return 0;
}