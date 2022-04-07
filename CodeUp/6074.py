"""
# 방법 1
c = ord(input())
t = ord('a')
while t <= c :
  print(chr(t), end=' ')
  t += 1
"""

# 방법 2
a = input()
count = 0
while(count <= ord(a) - 97):
    print(chr(97 + count), end=' ')
    count += 1