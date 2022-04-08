a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total *= b
print(total)

"""
모범 답안
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a * r

print(a)
"""