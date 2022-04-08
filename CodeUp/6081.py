n = input()
for i in range(1, 15 + 1):
	print('%X*%X=%X' %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))

"""
예시
...
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
...

참고
print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
작은 따옴표 2개 '' 또는 큰 따옴표 2개 "" 는 아무 문자도 없는 빈문자열(empty string)을 의미한다.
"""

"""
모범 답안
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
  
'''
또는
print("%X*%X=%X"%(n,i,n*i))
'''
"""