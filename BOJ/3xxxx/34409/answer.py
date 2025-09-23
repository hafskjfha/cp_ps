def main():
    INF=float('inf')
    input=open(0).readline
    n,m=map(int,input().split())
    sy,sx=map(int,input().split())
    a,b,c=map(int,input().split())
    mudngsan=[]
    max_height,mhx,mhy=0,0,0
    for i in range(n):
        temp=[*map(int,input().split())]
        for j in range(m):
            if temp[j]>max_height:
                max_height,mhx,mhy=temp[j],j,i
        mudngsan.append(temp)
    d=dijkstra(n,m,sx-1,sy-1,mudngsan,[[INF]*m for _ in range(n)],a,b,c)
    print([-1,d[mhy][mhx]][d[mhy][mhx]!=INF])

def dijkstra(n,m,sx,sy,gr,d,a,b,c):
    import heapq
    pop=heapq.heappop
    push=heapq.heappush
    d[sy][sx]=0
    heap=[(0,sx,sy)]
    while heap:
        w,x,y=pop(heap)
        if d[y][x]<w:continue
        nextc=((x+1,y),(x-1,y),(x,y+1),(x,y-1))
        for dx,dy in nextc:
            if 0<=dx<m and 0<=dy<n:
                diff=abs(gr[dy][dx]-gr[y][x])
                t=[diff*a,diff*b][gr[y][x]>gr[dy][dx]]if diff else 1
                if diff<=c and d[dy][dx]>w+t:
                    d[dy][dx]=w+t
                    push(heap,(d[dy][dx],dx,dy))
    return d

main()
