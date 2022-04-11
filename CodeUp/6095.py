li = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if(li[x - 1][y - 1] != 1):
        li[x - 1][y - 1] = 1
for i in li:
	print(' '.join(map(str, i)))

"""
모범 답안
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()
"""