#include <stdio.h>

int main() {
    char str;
    
    while (str != 'q') {
        scanf("%c", &str);
        printf("%c", str);
    }
  
    return 0;
}