from collections import deque
m,n,s=map(int,input().split())
a,b=[0]*n,[0]*n
for i in range(n):
    x,y=map(int,input().split())
    a[i],b[i]=x,y
q=deque([(s,0)])
v=set()
while q:
    x,t=q.popleft()
    for i in range(n):
        y=(x*a[i]+b[i])%m
        if y==0:exit(print(t+1))
        if y not in v:q.append((y,t+1));v.add(y)

print(-1)