from random import randint
n = int(input())
temp = [0] * 23
nums = input().split()
for i in nums:
    temp[int(i) - 1] += 1
for i in temp:
    print(i, end=' ')

"""
모범 답안
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')
"""