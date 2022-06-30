#include <stdio.h>

int main() {
    int num;
    
    checkpoint:
        scanf("%d", &num);
  
        if(num!=0) {
            printf("%d\n", num);
            goto checkpoint;
        }
    
    return 0;
}