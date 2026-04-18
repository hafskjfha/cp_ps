import sys

input=sys.stdin.readline

N=int(input())

for _ in range(N):

	h = int(input());	d={0:0,1:1,2:2,3:4,4:7}

	if h not in d:

		for i in range(5,h+1):

			d[i]=d[i-3]+d[i-2]+d[i-1]

	print(d[h])

		