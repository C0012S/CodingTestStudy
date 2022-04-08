w, h, b = map(int, input().split())
mb = round(((w * h * b) / 8 / 1024 / 1024), 2)
print('{:.2f} MB'.format(mb))

"""
모범 답안
w, h, b = input().split()
res = int(w) * int(h) * int(b) / 1024 / 1024 / 8

print('%.2f'%res,"MB")
"""