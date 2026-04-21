from collections import deque
def bfs(b,n,m,v,q):
    while q:
        x,y=q.popleft()
        for dx,dy in((-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and v[ny][nx]==0 and b[ny][nx]=='1':
                q.append((nx,ny))
                v[ny][nx]=1
n,m=map(int,input().split())
b=[input().split()for _ in range(n)]
v=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if b[i][j]=='1'and v[i][j]==0:
            v[i][j]=1
            bfs(b,n,m,v,deque([(j,i)]))
            ans+=1
print(ans)