li = []
for i in range(19):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(19):
        li[a - 1][j] = 1 if li[a - 1][j] != 1 else 0
        li[j][b - 1] = 1 if li[j][b - 1] != 1 else 0
for i in li:
    print(' '.join(map(str, i)))

"""
모범 답안
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i + 1][j + 1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
"""
