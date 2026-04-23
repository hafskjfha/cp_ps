def main():
    input=open(0).readline
    n,m=map(int,input().split())
    b=[[*map(int,input().split())]for _ in range(n)]
    ans=[]
    delta=((1,0),(0,1),(-1,0),(0,-1))
    v=[[[-1]*4for _ in range(m)]for _ in range(n)]
    for i in range(n):
        x,y,d=0,i,0
        while 1:
            dx,dy=delta[d]
            nx,ny=x+dx*b[y][x],y+dy*b[y][x]
            if 0<=nx<m and 0<=ny<n:
                if v[ny][nx][d]==i:
                    ans.append(str(i+1))
                    break
                else:
                    v[ny][nx][d]=i
                    x,y=nx,ny
                    d=(d+1)%4
            else:
                break
    print(len(ans))
    if ans:print(*ans)
main()