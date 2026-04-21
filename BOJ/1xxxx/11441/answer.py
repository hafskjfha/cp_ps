I=open(0).readline
T=int
n=T(I())
a=[*map(T,I().split())]
p=[0]*(n+1)
for i in range(n):p[i+1]=p[i]+a[i]
for _ in range(T(I())):
    x,y=map(T,I().split())
    print(p[y]-p[x-1])