a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total += b
print(total)

"""
모범 답안
a, d, n=input().split()

a = int(a)
d = int(d)
n = int(n)

s = a
for i in range(2, n + 1):
   s += d

print(s)
"""