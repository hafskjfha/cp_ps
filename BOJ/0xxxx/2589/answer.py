from collections import deque
delta=((0,-1),(0,1),(1,0),(-1,0))
def bfs(b,v,n,m,sx,sy,t):
    q=deque([(sx,sy,0)])
    v[sy][sx]=t
    maxv=-1
    while q:
        x,y,d=q.popleft()
        for dx,dy in delta:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and v[ny][nx]!=t and b[ny][nx]=='L':
                q.append((nx,ny,d+1))
                v[ny][nx]=t
                maxv=max(maxv,d+1)
    return maxv
def main():
    I=open(0).readline
    n,m=map(int,I().split())
    b=[I().strip()for _ in range(n)]
    v=[[0]*m for _ in range(n)]
    t=1
    ans=-1
    for i in range(n):
        for j in range(m):
            if b[i][j]=='L':
                ans=max(ans,bfs(b,v,n,m,j,i,t))
                t+=1
    print(ans)
main()