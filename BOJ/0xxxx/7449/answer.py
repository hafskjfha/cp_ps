from collections import deque
I=open(0).readline
n=int(I())
p=[[]for _ in range(n)]
for _ in range(n):
    k,c,*v=map(int,I().split())
    p[k]=v
a,b=map(int,I().split())
q=deque([(a,0)])
v=[1]*n
while q:
    x,d=q.popleft()
    for y in p[x]:
        if y==b:exit(print(a,b,d))
        if v[y]:
            v[y]=0
            q.append((y,d+1))