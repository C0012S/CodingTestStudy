YMD = input()
Y = YMD[:2] # [A:B] -> A 이상 B 미만 [A, B)
M = YMD[2:4] # YMD[2:4] -> YMD의 2 번째부터 3 번째 원소
D = YMD[4:]

print(Y, M, D)