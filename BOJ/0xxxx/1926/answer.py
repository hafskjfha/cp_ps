def main():
    n,m=map(int,input().split())
    p=[[*map(int,input().split())] for _ in "_"*n]
    from collections import deque
    v=[[0]*m for _ in "_"*n]
    a,l=0,0
    def bfs(sx,sy):
        q=deque([(sx,sy)])
        p[sy][sx]=2
        r=1
        while q:
            x,y=q.popleft()
            for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=dx<m and 0<=dy<n and p[dy][dx]==1:
                    q.append((dx,dy))
                    p[dy][dx]=2
                    r+=1
        return r
    for ax in range(m):
        for ay in range(n):
            if p[ay][ax]==1:
                a=max(a,bfs(ax,ay))
                l+=1
    print(l,a)
                    
        
main()