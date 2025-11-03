def main():
    input=open(0).readline
    n,m,k=map(int,input().split())
    b=[input().strip()for _ in range(n)]
    sx,sy,ex,ey=map(int,input().split())
    print(bfs(n,m,b,sy-1,sx-1,ey-1,ex-1,k))


def bfs(n,m,gr,sx,sy,ex,ey,k):
    from collections import deque
    INF=float('inf')
    d=[[INF]*m for _ in range(n)]
    delta=((1,0),(-1,0),(0,1),(0,-1))
    d[sy][sx]=0
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            return d[y][x]
        for dx,dy in delta:
            nx,ny=x,y
            for _ in range(k):
                nx,ny=nx+dx,ny+dy
                if not (0<=nx<m and 0<=ny<n) or gr[ny][nx]=='#':
                    break
                w=d[y][x]
                if d[ny][nx]>w+1:
                    d[ny][nx]=w+1
                    q.append((nx,ny))
                elif d[ny][nx]<w+1:break
                
    return -1
    
main()
