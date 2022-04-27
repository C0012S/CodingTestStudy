#include <stdio.h>

int main() {
    char word[51];
    scanf("%s", &word); // 문자열은 배열로 받아오므로 & 연산을 할 필요가 없어서 &word 대신 word만 적어도 된다.
    printf("%s", word);
    
    return 0;
}