a, m, d, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total = total * m + d
print(total)

"""
모범 답안
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a * m + d

print(a)
"""