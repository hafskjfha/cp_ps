# 34513 - bfs (460ms - pypy3 / 1736ms - python3)
def main():
    input=open(0).readline
    n=int(input())
    b=[]
    for i in range(n):
        t=input().strip()
        for j in range(n):
            if t[j]=='R':
                sx,sy=j,i
            elif t[j]=='K':
                ex,ey=j,i
        b.append(t)
    print(bfs(n,b,sx,sy,ex,ey))


def bfs(N,gr,sx,sy,ex,ey):
    from collections import deque
    INF=float('inf')
    WK='WK'
    d=[[INF]*N for _ in range(N)]
    delta=((1,0),(-1,0),(0,1),(0,-1))
    d[sy][sx]=0
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft()
        if x==ex and y==ey: return d[y][x]
        for dx,dy in delta:
            nx,ny=x,y
            while 1:
                nx,ny=nx+dx,ny+dy
                if not (0<=nx<N and 0<=ny<N) or gr[ny][nx]=='B':
                    break
                w=d[y][x]
                if d[ny][nx]>w+1:
                    d[ny][nx]=w+1
                    q.append((nx,ny))
                elif d[ny][nx]<w+1:break
                if gr[ny][nx] in WK:
                    break
    return -1
    
main()
