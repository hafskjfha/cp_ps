from collections import deque
delta=((-1,0),(1,0),(0,-1),(0,1))
zero='0'
def main():
    input=open(0).readline
    n,m=map(int,input().split())
    gr=[input().strip()for _ in range(n)]
    v=[[0]*m for _ in range(n)]
    ans=[[0]*m for _ in range(n)]
    gn=1
    gr_size={}
    walls=[]
    for y in range(n):
        for x in range(m):
            if gr[y][x]==zero:
                if v[y][x]==0:
                    s=bfs(gr,v,n,m,gn,x,y)
                    gr_size[gn]=s
                    gn+=1
            else:
                walls.append((x,y))
    for x,y in walls:
        ans[y][x]=1
        wallsv=set()
        for dx,dy in delta:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and gr[ny][nx]==zero and v[ny][nx] not in wallsv:
                ans[y][x]=(ans[y][x]+gr_size[v[ny][nx]])%10
                wallsv.add(v[ny][nx])
    for k in ans:
        print(''.join(map(str,k)))
def bfs(gr,v,n,m,gn,sx,sy):
    q=deque([(sx,sy)])
    v[sy][sx]=gn
    size=1
    while q:
        x,y=q.popleft()
        for dx,dy in delta:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and v[ny][nx]==0 and gr[ny][nx]==zero:
                q.append((nx,ny))
                size+=1
                v[ny][nx]=gn
    return size
main()