from collections import deque
n,m=map(int,input().split())
a,b=map(int,input().split())
drpan=[[None]*m for _ in range(n)]
drpan[a][b]='E'
delta=((-1,0,'E'),(1,0,'W'),(0,1,'N'),(0,-1,'S'))
q=deque([(b,a)])
while q:
    x,y=q.popleft()
    for dx,dy,dd in delta:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and drpan[ny][nx]is None:
            drpan[ny][nx]=dd
            q.append((nx,ny))
for p in drpan:
    print("".join(p))