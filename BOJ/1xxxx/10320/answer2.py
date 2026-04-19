from collections import deque
input=open(0).readline
for _ in range(int(input())):
    m,t=map(int,input().split())
    delta=[*map(int,input().split())]
    q=deque([(0,0)])
    ans=0,float('inf')
    v=set([0])
    while q:
        x,y=q.popleft()
        if x==t:
            ans=y,0
            break
        for dx in delta:
            nx=min(max(0,x+dx),3600)
            if 0<=nx<3601 and nx not in v:
                v.add(nx)
                q.append((nx,y+1))
                if 0<=nx-t<=ans[1]:ans=y+1,nx-t
    print(*ans)