a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# b와 c 먼저 비교해서 작은 것 선택, 그렇게 선택한 것과 a 비교해서 작은 것 선택
result =  a if a < (b if b < c else c) else (b if b < c else c)
# result = min(a, b, c)
print(result)