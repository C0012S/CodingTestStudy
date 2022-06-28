#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    
    if(a > 0) {
      printf("plus\n");
    }
    else {
      printf("minus\n");
    }
    
    if(a % 2 == 0) {
      printf("even\n");
    }
    else {
      printf("odd\n");
    }
    
    return 0;
}


/*
// 다른 방법
#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    
    if (a > 0) {
        printf("plus\n");
        if (a % 2 == 0) {
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
    }
    else if (a < 0) {
        printf("minus\n");
        if (a % 2 == 0) {
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
    }
    else {
        printf("zero\n");
    }
    
    return 0;
}
*/
