import sys
INF=float('inf')
input=sys.stdin.readline
N=int(input())
M=int(input())
gr=[[INF]*(N)for _ in range(N)]
for i in range(N):gr[i][i]=0
for _ in range(M):
	a,b,c=map(int,input().split())
	gr[a-1][b-1]=min(gr[a-1][b-1],c)
def floyd():
	for i in range(N):
		for j in range(N):
			for k in range(N):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
floyd()
for L in gr:
	for I in L:
		if I==INF:print(0,end=' ')
		else:print(I,end=' ')
	print()