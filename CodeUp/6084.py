h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))

"""
모범 답안
h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h * b * c * s / 8 / 1024 / 1024, 1), "MB")
"""