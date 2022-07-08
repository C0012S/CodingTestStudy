/*
3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.
*/

#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    
    for (int i = 1; i <= num; i++) {
        if (i == 3 || i == 6 || i == 9)	//if (i % 10 == 3 || i % 10 == 6 || i % 10 == 9)
            printf("X ");
        else
            printf("%d ", i);
    }
    
    return 0;
}