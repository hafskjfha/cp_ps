import sys
input=sys.stdin.readline
N=int(input())
m=list(map(int,input().split()))
a,b,c,d,e,f=m[0],m[1],m[2],m[0],m[1],m[2]
for _ in range(N-1):
	m=list(map(int,input().split()))
	a,b,c=max(a+m[0],b+m[0]),max(a+m[1],b+m[1],c+m[1]),max(b+m[2],c+m[2])
	d,e,f=min(d+m[0],e+m[0]),min(d+m[1],e+m[1],f+m[1]),min(e+m[2],f+m[2])
print(max(a,b,c),min(d,e,f))