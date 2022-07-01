#include <stdio.h>

int main() {
    int num;
  
    while (1) {
        scanf("%d", &num);
      
        if (num == 0) 
            break;
        printf("%d\n", num);
    }
  
    return 0;
}