#include <stdio.h>

int main() {
    int num1, num2; 
    scanf("%d", &num1);
    
    print_num:
        scanf("%d", &num2);
        printf("%d\n", num2);
  
        num1 -= 1;
        if(num1 > 0) goto print_num;
        
    return 0;
}