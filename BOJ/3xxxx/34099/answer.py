input=open(0).readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>1:print(*range(1,n+1))
    else:
        if n<4:print(-1)
        else:print(*range(2,n+1,2),*range(1,n+1,2))