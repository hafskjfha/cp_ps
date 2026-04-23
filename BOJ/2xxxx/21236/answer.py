input=open(0).readline
b=[[[0,None]for _ in range(1001)]for _ in range(1001)]
a=0
for _ in range(int(input())):
    x,y=map(int,input().split())
    b[y][x][1]=1
    if b[y][x][0]==3:a+=1
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx,ny=x+dx,y+dy
        if 0<=nx<1001 and 0<=ny<1001:
            if b[ny][nx][0]==3 and b[ny][nx][1] is not None:a-=1
            b[ny][nx][0]+=1
            if b[ny][nx][0]==3 and b[ny][nx][1] is not None:a+=1
    print(a)