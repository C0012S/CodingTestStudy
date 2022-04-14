li = []
for i in range(10):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
x, y = 1, 1
flag = True

while flag:
    if li[x][y] == 2:
        li[x][y] = 9
        flag = False
    elif (li[x][y + 1]) == 1:
        if li[x + 1][y] == 1:
            li[x][y] = 9
            flag = False
        else:
            li[x][y] = 9
            x += 1
    else:
        li[x][y] = 9
        y += 1
for i in li:
    print(' '.join(map(str, i)))

"""
모범 답안
m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i + 1][j + 1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y + 1]==1 and m[x + 1][y]==1) or (x == 9 and y == 9) :
    break

  if m[x][y + 1] != 1 :
    y += 1
  elif m[x + 1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
"""
