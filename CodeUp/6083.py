a, b, c = map(int, input().split())
count = 0
for i in range(a):
	for j in range(b):
		for k in range(c):
			print('{} {} {}'.format(i, j, k))
			count += 1
      
print(count)

"""
모범 답안
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r) :
  for j in range(0, g) :
    for k in range(0, b) :
      print(i, j, k)

print(r * g * b)
"""