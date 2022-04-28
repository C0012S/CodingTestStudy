#include <stdio.h>

int main() {
    char word[21];
    scanf("%s", word);
    for (int i = 0; word[i] != '\0'; i++) {
        printf("\'%c\'\n", word[i]);
    }
    
    return 0;
}