#include <stdio.h>

int main() {
    char a;
    scanf("%c", &a);	//%s도 가능
    printf("%c", a + 1);
  
    return 0;
}

// 입력되는 문자 1 개는 char 타입으로 받고, 출력 시에도 %c를 사용한다. 이때 입력받을 때는 %c말고 %s를 써도 되지만 %s는 하나의 단어(문장)을 받는 경우에 더 적절하다.