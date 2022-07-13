#include <stdio.h>

int main() {
    int num, sum = 0, i = 0;
    scanf("%d", &num);
    
    while (1) {
        sum += ++i;
        
        if (sum >= num) {
            printf("%d", sum);
            break;
        }
    }
  
    return 0;
}