from collections import deque
input=open(0).readline
N,T,W=map(int,input().split())
wq=deque()
for _ in range(N):
    wq.append([*map(int,input().split())])
a=[[*map(int,input().split())]for _ in range(int(input()))]
a.sort(key=lambda x:x[2])
a=deque(a)
nw=0
while W-nw>0:
    p,t=wq.popleft()
    for _ in range(T):
        print(p)
        t-=1
        nw+=1
        if a and a[0][2]==nw:
            mp,mt,mc=a.popleft()
            wq.append([mp,mt])
        if t==0:
            break
        if W-nw<=0:
            break
    if t and W-nw>0:
        wq.append([p,t])