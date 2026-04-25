def main():
    input=open(0).readline
    n,m=map(int,input().split())
    p=[input().strip()for _ in range(n)]
    c=0
    for y in range(n):
        for x in range(m):
            if p[y][x]=='.':continue
            for nx,ny in ((x+1,y),(x,y+1)):
                if 0<=nx<m and 0<=ny<n and p[ny][nx]!='.' and p[ny][nx]!=p[y][x]:
                    c+=1
    print(c)
main()