import sys

input=sys.stdin.readline

T=int(input())

for _ in range(T):

	P={1:1,2:1,3:1};	N=int(input())

	for i in range(4,N+1):

		P[i]=P[i-2]+P[i-3]

	print(P[N])