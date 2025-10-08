delta=((1,0,"E"),(-1,0,"W"),(0,1,"S"),(0,-1,"N"))
import sys
sys.setrecursionlimit(10**6)
def main():
    from collections import defaultdict
    input=open(0).readline
    n,m=map(int,input().split())
    city=[input().strip()for _ in range(n)]
    v=[[0]*m for _ in range(n)]
    c=0
    for sy in range(n):
        for sx in range(m):
            if v[sy][sx]==0:
                c+=dfs(sx,sy,v,city)
    print(c)

def move(x,y,p):
    for dx,dy,w in delta:
            nx,ny=x+dx,y+dy
            if w==p:
                return nx,ny
                
def dfs(x,y,v,city):
    if v[y][x]==1:return 1
    elif v[y][x]==2: return 0
    v[y][x]=1
    r=dfs(*move(x,y,city[y][x]),v,city)
    v[y][x]=2
    return r
    
main()