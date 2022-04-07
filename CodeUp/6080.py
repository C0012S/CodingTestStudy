# 방법 1
n, m = input().split()
for i in range(1, int(n) + 1):
  for j in range(1, int(m) + 1):
    print(i, j)

"""
# 방법 2
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print('{} {}'.format(i, j))
"""