# 34513 - 다익스트라 (2800ms - pypy3)
def main():
    input=open(0).readline
    n=int(input())
    b=[]
    for i in range(n):
        t=input().strip()
        b.append(t)
        for j in range(n):
            if t[j]=='R':
                sx,sy=j,i
            elif t[j]=='K':
                ex,ey=j,i
    print(dijkstra(n,b,sx,sy,ex,ey))

def dijkstra(N,gr,sx,sy,ex,ey):
    import heapq
    INF=float('inf')
    d=[[INF]*N for _ in range(N)]
    delta=((1,0),(-1,0),(0,1),(0,-1))
    d[sy][sx]=0
    heap=[(0,sx,sy)]
    while heap:
        w,x,y=heapq.heappop(heap)
        if x==ex and y==ey: return w
        if d[y][x]<w:continue
        for dx,dy in delta:
            nx,ny=x,y
            while 1:
                nx,ny=nx+dx,ny+dy
                if not (0<=nx<N and 0<=ny<N) or gr[ny][nx]=='B':
                    break
                if d[ny][nx]>w+1:
                    d[ny][nx]=w+1
                    heapq.heappush(heap,(d[ny][nx],nx,ny))
                elif d[ny][nx]<w+1:break
                if gr[ny][nx] in ('W','K'):
                    break
                    
                
    return -1
main()
