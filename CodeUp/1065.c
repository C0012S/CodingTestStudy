#include <stdio.h>

int main() {
    int a, b, c;
    int arr[3];
    
    scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
    
    for(int i = 0; i < 3; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d\n", arr[i]);
        }
    }
    
    return 0;
}


/*
# 다른 방법
int main() {
    int a, b, c;
    
    scanf("%d %d %d", &a, &b, &c);
    
    if(a % 2 == 0) {
        printf("%d\n", a);
    }
    
    if(b % 2 == 0) {
        printf("%d\n", b);
    }
    
    if(c % 2 == 0) {
        printf("%d\n", c);
    }
    
    return 0;
}
*/
